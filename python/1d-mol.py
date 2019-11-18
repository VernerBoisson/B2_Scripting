# !/usr/bin/python3
# 1d-mol.py
# Jeu du plus ou moins
# Verner Boisson
# 27 oct 2018

import random
import signal
import sys


# Fonction qui permet de quitter proprement
def quit(sig, frame):
    sys.exit(0)
    return


# Message d'aurevoir plus le résultat si on quitte le programme avec "q"
def byeMessage(number):
    string = str("La solution était "+str(number)+". Je vous souhaite une agréable journée.")
    print(string)
    return

# Initialisation du  nombre random et de la variable permettant la saisi
messages = {
    'input': 'Saisisez un nombre compris entre 0 et 100 \n',
    'erreurMax': "Le nombre doit être inférieur à 100 !",
    'erreurMin': "Le nombre doit être supérieur à 0 !",
    'petit': "C'est plus petit !",
    'grand': "C'est plus grand !",
    'gagne': "C'est gagné la solution était bien ",
    'erreurType': "Saisisez un nombre !"
}
random = random.random() * 100
str_input = -1

signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)


while int(str_input) != int(random):
    str_input = input(messages['input'])
    # Vérifie si c'est bien un nombre
    try:
        # Si l'utilisateur tape "q" alors ça quitte le programme
        if str(str_input) == 'q':
            byeMessage(int(random))
            break
        # Vérifie si le nombre est compris entre 0 et 100
        if int(str_input) < 0:
            print(messages['erreurMin'])
        elif int(str_input) > 100:
            print(messages['erreurMax'])
        else:
            # Le jeu du plus ou moins
            if int(str_input) > int(random):
                print(messages['petit'])
            elif int(str_input) < int(random):
                print(messages['grand'])
            else:
                print(messages['gagne']+str(int(random)))
    except:
        print(messages['erreurType'])
        str_input = -1
