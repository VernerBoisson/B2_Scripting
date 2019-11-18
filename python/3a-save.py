# !/usr/bin/python3
# 3a-save.py
# sauvegarde le coutenu du repertoire script dans le répertoire data
# Verner Boisson
# 06 nov 2018


import signal
import sys
from shutil import make_archive
import shutil
import os
import gzip


# Permet de supprimer l'archive si elle existe
def supp():
    if os.path.exists(archive_name+'.tar.gz'):
        os.remove(archive_name+'.tar.gz')
    return


# Fonction qui permet de quitter proprement
def quit(sig, frame):
    supp()
    sys.exit(0)
    return

signal.signal(signal.SIGTERM, quit)
signal.signal(signal.SIGINT, quit)


# Initialisation des variables
path_directory = os.path.expanduser('~/B2-Python/scripts')
archive_name = os.path.expanduser('~/my_archive')
path_data = os.path.expanduser('~/Data/')
error_messages = {
    'permission_source': 'Erreur : Pas les permissions nécessaires sur les fichiers pour faire l\'archive \n',
    'permission_destination': 'Erreur : Pas les permission nécessaire sur le répertoire de destination \n',
    'no_space': 'Erreur : Il n\'y a pas assez de place \n'
}
messages = {
    'confirmation': "La sauvegarde a bien été effectuer. \n",
    'existe': "La sauvegarde existe déjà. \n"
}

# Si le répertoire destination n'existe pas le créer
if not os.path.exists(path_data):
    os.makedirs(path_data)

# Check permission du répertoire destination
if os.access(path_data, os.R_OK | os.W_OK):
    # Essaie de créer l'archive
    try:
        make_archive(archive_name, 'gztar', path_directory)
        # S'il y a une ancienne sauvegarde les comparent
        if os.path.exists(path_data+'/my_archive.tar.gz'):
            with gzip.open(path_data+'/my_archive.tar.gz') as file:
                save_file = file.read()

            with gzip.open(archive_name+'.tar.gz') as file:
                new_save = file.read()

            if save_file != new_save:
                shutil.move(archive_name+'.tar.gz', path_data)
                sys.stdout.write(messages['confirmation'])
            else:
                supp()
                sys.stdout.write(messages['existe'])
        else:
            shutil.move(archive_name+'.tar.gz', path_data)
            sys.stdout.write(messages['confirmation'])

    except Exception as exception:
        supp()
        if(exception.args[0] == 13):
            sys.stderr.write(error_messages['permission_source'])
        elif(exception.args[0] == 27):
            sys.stderr.write(error_messages['no_space'])
        else:
            sys.stderr.write(str(exception.args[0]+' : '+str(exception.message)))
else:
    sys.stderr.write(error_messages['permission_destination'])
