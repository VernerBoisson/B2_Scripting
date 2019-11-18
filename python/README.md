# TP2 - Python

Vous pouvez utiliser une VM, un conteneur ou votre hôte pour ce TP. Seule condition : **Python3 up-to-date**. 

Pour chacun des exercices vous rendrez un fichier `.py` exécutable. 

N'hésitez pas à faire vos tests directement dans la console python, et à vous aider du [mémo pour la syntaxe de base](https://gist.github.com/It4lik/097def35b9abb53f0ce96334fba4d932).

Le nom des scripts est imposé encore une fois et est précisé pour chacun d'entre eux. Aussi, tous vos scripts devront avoir : 
* un en-tête
* des déclarations de fonctions
* des déclaration de variables 
* commentaire

## Rendu
#### Forme
Pour rappel, le rendu :
* doit être un dépôt GitHub
  * il doit s'appeler B2-Python
  * il doit comporter un répertoire `scripts/`
  * chacun des scripts rendus doivent se trouver à la racine de ce répertoire
    * Pour ceux qui ont besoin de plus d'un seul fichier pour un exercice donné, vous pouvez créer un répertoire qui porte le nom qu'aurait du porter le script sans l'extension `py`
    * `/scripts/2a-mol.py` **OU** `/scripts/2a-mol/` par exemple    
* les scripts
  * doivent comporter un shebang
  * doivent comprendre un en-tête
  
**Si un seul des points ci-dessus n'est pas respecté, aucune correction ne sera effectuée.**

#### Règles de style
Vos scripts doivent comprendre :
  * des commentaires sur les blocs de code qui ne sont pas explicites
  * des fonctions et variables nommées explicitement
  * **dans cet ordre** :
    * `import`s
    * optionnel : interception de signaux (`SIGINT` par exemple)
    * optionnel : parsing d'arguments (avec `argparse`)
    * définitions de fonctions
    * code

## 1. Manipulation de bases
### `1a-add.py`
Demander deux nombres à l’utilisateur et afficher le résultat de l’addition des deux
nombres.  
Contrôler que l’utilisateur a bien saisi deux nombres et pas autre chose.

### `1b-dic.py`
Demander une saisie utilisateur de plusieurs prénoms.  
L’utilisateur peut choisir d’arrêter la saisie en appuyant sur la touche ‘q’.  
Les stocker dans une liste. Afficher le résultat en ordonnant les prénoms par ordre alphabétique.

### `1c-moy.py`
Demander une saisie utilisateur de plusieurs notes et prénoms : 
* l'utilisateur saisit un prénom, et une note pour chacun d'entre eux
* l'utilisateur peut saisir 'q' pour stopper la saisie
* affichez ensuite la moyenne et un top 5 des meilleures notes
* hint : utiliser un dictionnaire python

### TODO
Réécrire les trois précédents scripts, et contrôler la saisie utilisateur. Pour l'addition par exemple, vérifier que l'utilisateur a bien saisi des nombres.  
Vous le ferez ensuite pour **TOUTES LES ENTREES UTILISATEURS** .  
### `1d-mol.py`
Jeu du plus ou moins :
* Générer un nombre aléatoire (entre 0 et 100 par exemple).
* Demander une saisie utilisateur tant qu’il ne trouve pas le nombre que vous avez généré.
* Afficher à chaque nombre saisi s’il est plus grand ou pus petit que le nombre que vous avez généré.  

Dans un second temps : 
* Créez une fonction qui affiche un message d'au revoir et la solution
* Permettez à l'utilisateur de quitter le jeu en tapant 'q', cela appelle la fonction précédente
* Si l'uttilisateur coupe le script avec `CTRL + C` vous devrez aussi appeler une fonction qui quitte proprement le programme
  * pour ce faire utiliser le module `signal`
  * quand vous faites `CTRL + C` vous envoyez un 'signal' au processus python (votre programme qui tourne) : un `SIGINT`. Il nous suffit de l'intercepter, exemple : 
```python
import signal
from time import sleep

def youcant(sig, frame):
    print('You cant CTRL+C on me !')

signal.signal(signal.SIGINT, youcant)

i = 0
while True:
    print(i)
    sleep(1)
    i += 1
```
* (juste en passant, un `kill <PID>`, commande qui permet de tuer un processus, ça envoie un `SIGTERM`, on peut aussi l'intercepter)

## 2. Next step
### `2a-mol.py`
Jeu du plus ou moins qui lit dans un fichier. Il doit pouvoir tourner en permanence (avec quelque chose comme un `while True:`) et s'arrêter uniquement quand la solution aura été trouvée. Pour ce faire :
* écrire dans un fichier un message de bienvenue
* l'utilisateur peut saisir un nombre dans ce fichier
* votre programme doit lire le nombre et écrire 'plus' ou 'moins' dans le fichier

### `2b-auto.py`
Ecrire un programme qui résout le programme précédent.

## 3. Sauvegarde
### `3a-save.py`
Modules à regarder : `shutil`, `gzip`, `os`, `sys`)
Ecrire un script qui permet d’effectuer une sauvegarde: 
Votre outil doit :
* archiver et compresser (en `.tar.gz`) le répertoire choisi
* déplacer la sauvegarde dans un répertoire `data` créé à cet effet.
* la sauvegarde ne doit être déplacée dans le répertoire `data` uniquement si elle est différente de la précédente
* utiliser le module `sys` pour afficher des informations dans la sortie standard plutôt qu’avec `print`
* utiliser aussi `sys` pour retourner un code d’erreur spécifique en cas d’échec du programme
* utiliser le module `signal` pour intercepter le signal `SIGINT` et effectuer une action personnalisée.
* gérer les exceptions et affichez dans la sortie d’erreur un texte personnalisé en cas d’échec d’une étape importante (pas les droits sur le fichier, ou sur la destination, ou encore, en cas de remplissage du disque par exemple). 

Allez-y étape par étape et commencer par un archivage simple :)

### `3b-opt.py`
Le même script que le précédent mais en plus il doit disposer d'options au lancement pour :
* `-h` : un help pour le reste
* permettre de choisir un répertoire à sauvegarder en le passant en option de lancement
  * plusieurs répertoires pourront être gérés en un seul appel au script
* choisir le chemin du répertoire `data`

### `3c-ssh.py`
On continue.  
Si l’utilisateur le souhaite, il peut choisir de copier l’archive résultante sur un serveur distant SSH.  
Les options permettront de préciser un utilisateur et un mot de passepour la connexion SSH.  
Pour ce faire, vous pouvez utiliser le module `paramiko` et le module scp suivant : https://github.com/jbardin/scp.py (par exemple)

### `3d-daemon.py`
Votre script évolue, encore :
* il doit pouvoir tourner en démon pour surveiller la taille d'un répertoire
* au dessus d'un seuil critique, il doit déplacer le contenu après l'avoir archivé dans un répertoire `data` prévu à cet effet et effacer l'ancien contenu du répertoire
* le script dispose d'un fichier de configuration (plus pratique que des options quand ça devient complexe). On peut y préciser : 
  * x répertoires à surveiller
  * une destination pour d'un serveur SSH distant
  
### `3e-backup.service` ? 
Besoin d'un OS avec `systemd` pour cette partie. La VM CentOS7 des cours précédents peut faire l'affaire. 
Vous allez créer un fichier `.service` simple qui permet de démarrer et arrêter votre script. 
Autrement dit, on pourra : 
* configurer votre service de backup avec un fichier de configuration
* démarrer ou arrêter le service avec `systemctl start super-backup` et `systemctl stop super-backup`

En livraison pour cette étape on a : 
* l'application de backup : `3d-daemon.py`
  * avec un `-h` bien fait
  * on peut tester des backups directement en ligne de commande avec les options (`3c-ssh.py`)
* un fichier de configuration d'exemple
  * pour une configuration plus complexe et pérenne
* une unité de service systemd
  * pour gérer le service comme les autres services du système
* bonus : un fichier de log 
  * le contenu est libre à vous, s'inspirer de fichiers de logs existants peut donner des idées
 
## 4. HIDS
### `4a-hids.py`

La fonction de cet outil est bien différente. Mais si vous m'avez suivi jusque là, dans la mise en place technique c'est assez similaire.  
Un **HIDS** (*HostBased Intrusion Detection System*) **est un outil de détection d'intrusion**. Une des fonctions de base est de surveiller des répertoires ou des fichiers.  
En cas de changement de l'un d'entre eux, il effectue un rapport.  

Votre script doit :
* **surveiller une liste de répertoire et de fichiers** (fichier de conf ?) 
* doit permettre plusieurs méthodes pour **vérifier l'état des fichiers**. Par exemple :
  * nom
  * taille
  * date de modification
  * hash
* pour ce faire, vous devrez **conserver les données** au fil des exécutions du script :
  * un fichier simple en `json` par exemple
  * une base de données pour les motivés (`redis`, `mysql`, ou autres). Redis est très simple à utiliser (mais très puissant), c'est un simple système de clé/valeur. Je pourrai vous indiquer comment en mettre un en place rapidement si vous le souhaitez.
* en cas de détection d'un changement, il doit **effectuer une alerte** : écrire dans un **fichier de log**

**Bonus** : 
* créer une **unité de service systemd** pour gérer l'HIDS
* si vous craquez : créer une **API HTTP** simpliste qui permet de récupérer les alertes simplement :
  * une action pour lister toutes les alertes
  * une action pour lister une alerte (avec son ID)
  * une action pour récupérer la liste des dossiers surveillés
  * une action pour récupérer les alertes d'un dossier (avec son ID)
  * un fichier de log en `json` peut être utile pour être facilement parsable 