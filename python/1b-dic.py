# !/usr/bin/python3
# 1b-dic.py
# Affiche une liste de prénom saisie
# Verner Boisson
# 27 oct 2018


# Importation de la bibliothèque pour utiliser les REGEX
import re
import signal
import sys


# Fonction qui permet de quitter proprement
def quit(sig, frame):
    sys.exit(0)
    return


signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)


# Initialisation des variables
list = []
string = ""
regex = r"[a-zA-Z][^#&<>\"~;$^%{}?]"
messages = {
    'input': 'Saisisez un prénom ou q pour arrêter : ',
    'error': 'Veuilliez rentrer un prénom valide !'
}


# Saisi Utilisateur et vérification de la saisie
while string != 'q':
    string = input(messages['input'])
    if string != 'q':
        if re.match(regex, string) is not None:
            list.append(string)
        else:
            print(messages['error'])


list.sort()
print(list)
