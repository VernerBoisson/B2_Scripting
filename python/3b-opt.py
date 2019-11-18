# !/usr/bin/python3
# 3b-opt.py
# Sauvegarde le contenu de repertoires dans une archive tar.gz dans le répertoire choisi
# Verner Boisson
# 06 nov 2018


import signal
import sys
from shutil import make_archive
import shutil
import os
import gzip
import argparse


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


def compare_file(path_file):
    with gzip.open(path_file+'.tar.gz') as file:
        save_file = file.read()

    with gzip.open(path_file+'2.tar.gz') as file:
        new_save = file.read()

    if save_file != new_save:
        shutil.move(path_file+'2.tar.gz', path_file+'.tar.gz')
        sys.stdout.write(messages['confirmation'])
    else:
        supp()
        sys.stdout.write(messages['exists'])
    return


signal.signal(signal.SIGTERM, quit)
signal.signal(signal.SIGINT, quit)


# Initialisation des variables
parser = argparse.ArgumentParser(description='fait une archive d\'un répertoire vers un autre')
parser.add_argument('path_source', type=str, help="répertoires sources séparé par des ,")
parser.add_argument('path_dest', type=str, help="répertoire destination")
args = parser.parse_args()

for source in args.path_source.split(","):
    archive_name = source.split('/')
    # Pour que ça puisse prendre en compte un répertoire qui fini avec / ou non
    if(archive_name[-1] == ''):
        archive_name = archive_name[-2]
    else:
        archive_name = archive_name[-1]

    error_messages = {
        'permission_source': 'Erreur : Pas les permissions nécessaires sur les fichiers pour faire l\'archive \n',
        'permission_destination': 'Erreur : Pas les permissions nécessaires sur le répertoire de destination \n',
        'no_space': 'Erreur : Il n\'y a pas assez de place \n'
    }
    messages = {
        'confirmation': "La sauvegarde a bien été effectuer. \n",
        'exists': "La sauvegarde existe déjà. \n"
    }
    path_dest = os.path.expanduser(args.path_dest)
    path_source = os.path.expanduser(source)

    # Si le répertoire destination n'existe pas le créer
    if not os.path.exists(path_dest):
        os.makedirs(path_dest)
    # Check permission du répertoire destination
    if os.access(path_dest, os.R_OK | os.W_OK):
        # Essaie de créer l'archive
        try:
            make_archive(path_dest+archive_name+'2', 'gztar', path_source)

            # S'il y a une ancienne sauvegarde les comparent
            if os.path.exists(path_dest+archive_name+'.tar.gz'):
                compare_file(path_dest+archive_name)
            else:
                shutil.move(path_dest+archive_name+'2.tar.gz', path_dest+archive_name+'.tar.gz')
                sys.stdout.write(messages['confirmation'])
        except Exception as exception:
            supp()
            if(exception.args[0] == 13):
                sys.stderr.write(error_messages['permission_source'])
            elif(exception.args[0] == 27):
                sys.stderr.write(error_messages['no_space'])
            else:
                sys.stderr.write(str(exception.args[0])+' : '+str(exception.message))
    else:
        sys.stderr.write(error_messages['permission_destination'])
