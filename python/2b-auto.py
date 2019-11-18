# !/usr/bin/python3
# 2b-auto.py
# Resout Jeu du plus ou moins (2a-mol.py)
# Verner Boisson
# 27 oct 2018


import signal
import sys
import time


# Fonction qui permet de quitter proprement
def quit(sig, frame):
    sys.exit(0)
    return


# Fonction qui permet d'écrire dans le fichier
def writeFile(number, filename):
    fichier = open(filename, "a")
    fichier.write(str(number))
    fichier.close()


signal.signal(signal.SIGTERM, quit)
signal.signal(signal.SIGINT, quit)


# Initialisation
nom_fichier = "jeu_mol.txt"
nombre = 50
max = 101
min = -1
boolean = True


# Ecrit un nombre toutes les 6 secondes dans le fichier jeu_mol
# Commence par le nombre 50 puis prend la moitié restante à chaque fois
# Affiche dans la console lorsque c'est terminé ou s'il y a une erreur
writeFile(nombre, nom_fichier)
time.sleep(6)
while boolean:
    fichier = open(nom_fichier, "r")
    mots = fichier.readline()
    if "grand" in mots:
        min = nombre
        nombre += (max-min)/2
        nombre = int(nombre)
        writeFile(nombre, nom_fichier)
        time.sleep(6)
    elif "petit" in mots:
        max = nombre
        nombre -= (max-min)/2
        nombre = int(nombre)
        writeFile(nombre, nom_fichier)
        time.sleep(6)
    else:
        print(mots)
        boolean = False
    fichier.close()
