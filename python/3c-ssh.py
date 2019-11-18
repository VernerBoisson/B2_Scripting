# !/usr/bin/python3
# 3c-ssh.py
# Sauvegarde le contenu de répertoires dans une archive tar.gz dans le répertoire choisi à travers SSH
# Verner Boisson
# 10 nov 2018


import signal
import sys
from shutil import make_archive
import shutil
import os
import gzip
import argparse
from paramiko import SSHClient
from scp import SCPClient
from subprocess import call


# Permet de supprimer l'archive si elle existe
def supp():
    if os.path.exists(path_dest+archive_name+'2.tar.gz'):
        os.remove(path_dest+archive_name+'2.tar.gz')
    return


# Fonction qui permet de quitter proprement
def quit(sig, frame):
    supp()
    sys.exit(0)
    return

signal.signal(signal.SIGTERM, quit)
signal.signal(signal.SIGINT, quit)


# Initialisation des variables
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

parser = argparse.ArgumentParser(description='fait une archive d\'un répertoire vers un autre')
parser.add_argument('path_source', type=str, help="répertoires sources séparé par des ,")
parser.add_argument('path_dest', type=str, help="répertoire destination")
parser.add_argument('address_ip', type=str, help="adresse ip pour ssh")
parser.add_argument('username', type=str, help="username du ssh")
parser.add_argument('password', type=str, help="password du ssh")
args = parser.parse_args()

if args.address_ip:
    if args.username and not args.password:
        try:
            ssh = SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(args.address_ip, username=args.username)
            scp = SCPClient(ssh.get_transport())
        except Exception as exception:
            sys.stderr.write(error_messages['conn_fail'])
            sys.exit(0)
    elif args.username and args.password:
        try:
            ssh = SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(args.address_ip, username=args.username, password=args.password)
            scp = SCPClient(ssh.get_transport())
        except Exception as exception:
            sys.stderr.write(error_messages['conn_fail'])
            sys.exit(0)
    else:
        try:
            ssh = SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(args.address_ip)
            scp = SCPClient(ssh.get_transport())
        except Exception as exception:
            sys.stderr.write(error_messages['conn_fail'])
            sys.exit(0)
    for source in args.path_source.split(","):
        archive_name = source.split('/')
        # Pour que ça puisse prendre en compte un répertoire qui fini avec / ou non
        if(archive_name[-1] == ''):
            archive_name = archive_name[-2]
        else:
            archive_name = archive_name[-1]

        path_dest = os.path.expanduser("~")
        path_source = os.path.expanduser(source)
        path_dest_ssh = os.path.expanduser(args.path_dest)
        # Essaie de créer l'archive
        try:
            make_archive(path_dest+archive_name+'2', 'gztar', path_source)

            try:
                save_file = scp.get(path_dest_ssh+archive_name+'.tar.gz')
                save_file = save_file.read()

                with gzip.open(path_dest+archive_name+'2.tar.gz') as file:
                    new_save = file.read()
                if save_file != new_save:
                    shutil.move(path_dest+archive_name+'2.tar.gz', path_dest+archive_name+'.tar.gz')
                    try:
                        scp.put(path_dest+archive_name+'.tar.gz', remote_path=path_dest_ssh)
                        sys.stdout.write(messages['confirmation'])
                    except Exception as exception:
                        sys.stderr.write(error_messages['permission_destination'])
                        supp()
                else:
                    supp()
                    sys.stdout.write(messages['exists'])
                scp.close()
            except Exception as exception:
                sys.stderr.write(error_messages['permission_destination'])
        except Exception as exception:
            supp()
            if(exception.args[0] == 13):
                sys.stderr.write(error_messages['permission_source'])
            elif(exception.args[0] == 27):
                sys.stderr.write(error_messages['no_space'])
            else:
                sys.stderr.write(str(exception.args[0])+' : '+str(exception.message))
else:
    call(["python3", "3b-opt.py", args.path_source, args.path_dest])
