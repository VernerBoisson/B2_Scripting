# !/usr/bin/python3
# 1c-moy.py
# Affiche la moyenne d'une evaluation
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

dicNameMark = {}
messages = {
    "inputNom": "Saisisez un prénom ou q pour arrêter :",
    "inputNote": "Saisisez une note : ",
    "erreurNom": "Le prénom n'est pas valide !",
    "erreurNote": "La note n'est pas valide !",
    "erreurNoteBorn": "La note doit être comprise entre 0 et ",
    "inputBorn": "Saisisez la note maximal possible lors de l'évaluation (20 par défaut) : ",
    "erreurBorn": "Les notes sont sur ",
    "moyenne": "La moyenne de la classe est de : "
}
inputName = ""
regex = r"[a-zA-Z][^#&<>\"~;$^%{}?]"
mark_input = 0
sum_marks = 0
totalNbNotes = 0
born_note = 0


# Choix des bornes des notes.
try:
    born_note = input(messages['inputBorn'])
    born_note = int(born_note)
except:
    born_note = 20

print(messages['erreurBorn']+str(born_note))


# Saisi Utilisateur et vérification de la saisie
while inputName != 'q':
    inputName = input(messages['inputNom'])
    if inputName != 'q':
        if re.match(regex, inputName) is not None:
            mark_input = input(messages['inputNote'])
            mark_input = str(mark_input)
            try:
                if float(mark_input) >= 0 and float(mark_input) <= int(born_note):
                    dicNameMark[inputName] = float(mark_input)
                else:
                    print(messages['erreurNoteBorn']+str(born_note))
            except:
                print(messages['erreurNote'])
        else:
            print(messages['erreurNom'])


# Calcule de la moyenne
for key, val in dicNameMark.items():
    sum_marks += val
    totalNbNotes += 1


# Affichage de la moyenne
print(messages['moyenne']+str(sum_marks/totalNbNotes))


# Trie en fonction des notes
liste = sorted(dicNameMark.items(), key=lambda x: x[1], reverse=True)

# Afficher les 5 meilleur note
for note in range(5):
    if note < totalNbNotes:
        print(liste[note])
