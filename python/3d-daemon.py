# !/usr/bin/python3
# 3d-daemon.py
# Daemon : sauvegarde le contenu du répertoire lorsqu'il dépasse un certain seuil
# Verner Boisson
# 10 nov 2018


"""Generic linux daemon base class for python 3.x."""

import sys, os, time, atexit, signal
from shutil import make_archive
import shutil
import gzip
from paramiko import SSHClient
from scp import SCPClient

error_messages = {
    'permission_source': 'Erreur : Pas les permissions nécessaires sur les fichiers pour faire l\'archive \n',
    'permission_destination': 'Erreur : Pas les permissions nécessaires sur le répertoire de destination \n',
    'no_space': 'Erreur : Il n\'y a pas assez de place \n',
    'conn_fail': 'Connection Failed \n'
}
messages = {
    'confirmation': "La sauvegarde a bien été effectuer. \n",
    'exists': "La sauvegarde existe déjà. \n"
}


class daemon:
	"""A generic daemon class.

	Usage: subclass the daemon class and override the run() method."""

	def __init__(self, pidfile): self.pidfile = pidfile
	
	def daemonize(self):
		"""Deamonize class. UNIX double fork mechanism."""

		try: 
			pid = os.fork() 
			if pid > 0:
				# exit first parent
				sys.exit(0) 
		except OSError as err: 
			sys.stderr.write('fork #1 failed: {0}\n'.format(err))
			sys.exit(1)
	
		# decouple from parent environment
		os.chdir('/') 
		os.setsid() 
		os.umask(0) 
	
		# do second fork
		try: 
			pid = os.fork() 
			if pid > 0:

				# exit from second parent
				sys.exit(0) 
		except OSError as err: 
			sys.stderr.write('fork #2 failed: {0}\n'.format(err))
			sys.exit(1) 
	
		# redirect standard file descriptors
		sys.stdout.flush()
		sys.stderr.flush()
		si = open(os.devnull, 'r')
		so = open(os.devnull, 'a+')
		se = open(os.devnull, 'a+')

		os.dup2(si.fileno(), sys.stdin.fileno())
		os.dup2(so.fileno(), sys.stdout.fileno())
		os.dup2(se.fileno(), sys.stderr.fileno())
	
		# write pidfile
		atexit.register(self.delpid)

		pid = str(os.getpid())
		with open(self.pidfile,'w+') as f:
			f.write(pid + '\n')
	
	def delpid(self):
		os.remove(self.pidfile)

	def start(self):
		"""Start the daemon."""

		# Check for a pidfile to see if the daemon already runs
		try:
			with open(self.pidfile,'r') as pf:

				pid = int(pf.read().strip())
		except IOError:
			pid = None
	
		if pid:
			message = "pidfile {0} already exist. " + \
					"Daemon already running?\n"
			sys.stderr.write(message.format(self.pidfile))
			sys.exit(1)
		
		# Start the daemon
		self.daemonize()
		self.run()

	def stop(self):
		"""Stop the daemon."""

		# Get the pid from the pidfile
		try:
			with open(self.pidfile,'r') as pf:
				pid = int(pf.read().strip())
		except IOError:
			pid = None
	
		if not pid:
			message = "pidfile {0} does not exist. " + \
					"Daemon not running?\n"
			sys.stderr.write(message.format(self.pidfile))
			return # not an error in a restart

		# Try killing the daemon process	
		try:
			while 1:
				os.kill(pid, signal.SIGTERM)
				time.sleep(0.1)
		except OSError as err:
			e = str(err.args)
			if e.find("No such process") > 0:
				if os.path.exists(self.pidfile):
					os.remove(self.pidfile)
			else:
				print (str(err.args))
				sys.exit(1)

	def restart(self):
		"""Restart the daemon."""
		self.stop()
		self.start()

	def run(self):
		"""You should override this method when you subclass Daemon.
		
		It will be called after the process has been daemonized by 
		start() or restart()."""

        with open("config.txt", "r") as file:
            for line in file:
                if line == 1:
                    path_source = line.read()
                if line == 2:
                    path_dest = line.read()
                if line == 3:
                    ip_address = line.read()
                if line == 4:
                    username = line.read()
                if line == 5:
                    password = line.read()
                if line == 6:
                    limit = line.read()

        for source in path_source.split(","):
            archive_name = source.split('/')
            if(archive_name[-1] == ''):
                archive_name = archive_name[-2]
            else:
                archive_name = archive_name[-1]

            statinfo = os.stat(source)
            if statinfo.st_size > limit:
                # Si SSH
                if ip_address:
                    if username and not password:
                        ssh = SSHClient()
                        ssh.load_system_host_keys()
                        ssh.connect(ip_address, username=username)
                        scp = SCPClient(ssh.get_transport())
                    elif username and password:
                        ssh = SSHClient()
                        ssh.load_system_host_keys()
                        ssh.connect(ip_address, username=username, password=password)
                        scp = SCPClient(ssh.get_transport())
                    else:
                        ssh = SSHClient()
                        ssh.load_system_host_keys()
                        ssh.connect(ip_address)
                        scp = SCPClient(ssh.get_transport())
                    
                    path_dest_ssh = os.path.expanduser(path_dest)
                    path_dest = os.path.expanduser("~")
                    path_source = os.path.expanduser(source)
                    try:
                        make_archive(path_dest+archive_name, 'gztar', path_source)
                        try:
                            save_file = scp.get(path_dest_ssh+archive_name+'.tar.gz')
                            save_file = save_file.read()

                            with gzip.open(path_dest+archive_name+'.tar.gz') as file:
                                new_save = file.read()
                            if save_file != new_save:
                                try:
                                    scp.put(path_dest+archive_name+'.tar.gz', remote_path=path_dest_ssh)
                                    os.remove(path_dest+archive_name+'.tar.gz')
                                    sys.stdout.write(messages['confirmation'])
                                except Exception as exception:
                                    sys.stderr.write(error_messages['permission_destination'])
                            else:
                                sys.stdout.write(messages['exists'])
                            scp.close()
                        except Exception as exception:
                            sys.stderr.write(error_messages['permission_destination'])
                    except Exception as exception:
                        sys.stderr.write(error_messages['permission_destination'])
                # Si Pas SSH
                else:
                    try:
                        make_archive(path_dest+archive_name, 'gztar', path_source)
                    except Exception as exception:
                        if(exception.args[0] == 13):
                            sys.stderr.write(error_messages['permission_source'])
                        elif(exception.args[0] == 27):
                            sys.stderr.write(error_messages['no_space'])
                        else:
                            sys.stderr.write(str(exception.args[0])+' : '+str(exception.message))
