# !/usr/bin/python3
# 2a-mol.py
# Jeu du plus ou moins (avec fichier)
# Verner Boisson
# 27 oct 2018

import random
import signal
import sys
import time


# Fonction qui permet de quitter proprement
def quit(sig, frame):
    sys.exit(0)
    return

signal.signal(signal.SIGTERM, quit)
signal.signal(signal.SIGINT, quit)


# Fonction qui permet d'écrire un message dans un fichier
def writeFile(message, nomfichier):
    filetmp = open(nomfichier, "w")
    filetmp.write(message)
    filetmp.close()
    return


# Le jeu du plus ou moins
def mol(arg_input, random, file_name):
    if arg_input > random:
        writeFile(messages['moins'], file_name)
    elif arg_input < random:
        writeFile(messages['plus'], file_name)
    else:
        writeFile(messages['gagner']+str(random), file_name)
    return


# Initialisation des variables
born_max = 100
random = random.random() * born_max
file_name = "jeu_mol.txt"
messages = {
    'defaut': 'Veuillez entrer un nombre compris entre 0 et '+str(born_max)+' à la ligne 2 : \n',
    'born_min': 'Le nombre doit être supérieur à 0 ! \n',
    'born_max': 'Le nombre doit être inférieur à '+str(born_max)+' ! \n',
    'moins': 'C\'est plus petit ! \n',
    'plus': 'C\'est plus grand ! \n',
    'gagner': 'C\'est gagné la solution était bien ',
    'nombre': 'Saisisez un nombre ! \n'
}
targetline = [2]
int_input = -1


writeFile(messages['defaut'], file_name)


while int(int_input) != int(random):
    file = open(file_name, "r")
    compteur = 0
    for line in file.readlines():
        # Le compteur permet de vérifier uniquement la deuxième ligne
        compteur += 1
        if compteur == 2:
            int_input = line
            # Vérifie si la saisi est un nombre
            try:
                # Vérifie si le nombre est compris entre 0 et 100
                if int(int_input) < 0:
                    writeFile(messages['born_min'], file_name)
                elif int(int_input) > born_max:
                    writeFile(messages['born_max'], file_name)
                else:
                    mol(int(int_input), int(random), file_name)
            except:
                writeFile(messages['nombre'], file_name)
                int_input = -1
    file.close()
    time.sleep(2)
