# !/usr/bin/python3
# 1a-add.py
# Additionne deux nombre saisis
# Verner Boisson
# 27 oct 2018


import signal
import sys


# Fonction qui permet de quitter proprement
def quit(sig, frame):
    sys.exit(0)
    return


signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)


# Saisi Utilisateur et vérification de la saisie et Affichage de l'addition
int1 = input('Nombre 1 : ')
int2 = input('Nombre 2 : ')
try:
    result = float(int1)+float(int2)
    result = str(result)
    print("Le resultat de l'addition est : "+result)
except:
    print('Saisisez des nombres !')
