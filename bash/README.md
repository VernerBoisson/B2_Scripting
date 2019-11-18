# TP1 : Fondamentaux du shell GNU/Linux & Bash

EDIT : [mémo `bash`](https://gist.github.com/It4lik/aa461ba25449581fb2d1612f086f1dd8)

Tout le monde sur du CentOS pendant mes TPs ! :) Et à jour svp.

Ce TP a pour objectif de revoir un peu les fondamentaux de `bash` et de commencer à rédiger quelques scripts.

Par "scripting", nous entendons du développement simple, court, efficace et **proche du système** (et parfois un peu de bricolage, mais il ne faut pas le dire).

gl hf

## Mémo Bash

### Commandes 

`<commande> --help` ou `man <commande>` pour plus d’infos !

* `pwd` : afficher le dossier courant
*  `ls`  : lister fichiers et dossiers dans le dossier courant
* `cd` : changer de dossier
* `cp` : copier un fichier 
* `mv` : déplacer (ou renommer !) un fichier 
* `ln` : créer un lien
* `rm` : supprimer un fichier (-r pour un dossier)
* `whoami` : afficher utilisateur courant
*`cat` : ouvrir un fichier
* `mkdir` : créer un dossier vide
* `touch` : créer un fichier vide
* `chmod` : changer les permissions d’un fichier
* `chown` : changer le propriétaire d’un fichier 

### Syntaxe des blocs conditionnels

* Bloc IF
```bash
if [[ confidition   ]] 
then
	<instructions>
fi
```
* Bloc WHILE
```bash
while [[ condition ]] 
do
	<instructions>
done
```

Pour exécuter un script, il faut le rendre exécutable : 
`chmod +x <fichier>`
Et pour le lancer : 
`./fichier`

----  

**Pour chaque question, créer un script `bash` exécutable.** (comment ça c'est pas des questions ?)
**Je vous impose le nom du script, il est précisé juste en dessous du titre pour chacune des questions**. Ca m'évite de mourir quand je corrige. DESO de limiter votre créativité, ça laissera plus de place pour vous exprimer dans les scripts :)

### 1. `date`
Name : `1date`

Afficher la date au format suivant :   
`Nous sommes lundi, le 25 septembre de 2017`

### 2. Utilisateurs système
Name : `2users`  
**a.** Listez les utilisateurs grâce au fichier `/etc/passwd`  
**b.** A l’aide de la commande `cut`, filtrez uniquement le **nom** des utilisateurs (utiliser un délimiteur avec l'option `-d`) et le shell qu'ils utilisent

### 3. Paquets & Ressources système
Name : `3ress`  
Installer le paquet `htop`, et le lancer pour observer un peu l’état de votre machine.  
Pour chercher un paquet : `yum search`, pour installer : `yum install`  
Vous pouvez aussi installer le paquet `sl`... (pour la petite histoire, c'est un troll pour le gens qui se plantent en tapant mal `ls`)  
**a.** Installez le paquet `sysstat`. Créez un script qui affiche la RAM libre sur le système (infos RAM avec `free`), le pourcentage d'occupation de la partition montée sur `/` (infos stockage avec `df`) et l'utilisation CPU (infos CPU avec `sar`).  

### 4. Script d'appréciations
Name : `4appr`  

**a.** Ecrire un script qui détermine l’appréciation d’une note. Le script attend une saisie utilisateur (commande `read`) et affiche une appréciation en fonction de la note saisie.  

0-5 : “passable”  
6-10 : “insuffisant”  
11-15 : “bien”  
16-20 : “excellent”  
  
**b.** Contrôler la saisie de l’utilisateur pour nombre entre 0 et 20, ou afficher un message d’erreur  
**c.** Vérifier que la saisie utilisateur est un nombre, ou afficher un message d’erreur  

### 5. Moyenne
Name : `5moy`  

Ecrire un script qui effectue la moyenne de plusieurs notes saisies. (Par exemple, l’utilisateur sépare les notes avec espace ou en appuyant sur entrée. Il peut arrêter la saisie en appuyant sur ‘q’.)  

Si la saisie n'est pas une note, afficher un message d'erreur ('ceci n'est pas une note'), ignorer le mot saisi, et demander la prochaine saisie. 

### 6. Cherchez un peu de la doc ! 
Name : `6state`

Créez un script résumant un peu l'état de la machine actuelle. Il doit afficher :
* le hostname de la machine et son IP (IP utilisée pour se connecter en SSH)
* le nom et la version de l'OS
* la version du kernel utilisé par l'OS
* les 5 derniers utilisateurs qui se sont loggés dans la machine
* les 3 derniers paquets installés
* si oui ou non la commande `python` est disponible
* si oui ou non le service SSH est activé

### 7. Plus ou moins
Name : `71mol` et ses potes `72mol` et `73mol`

Ecrire un script “plus ou moins”.  

**a.** Le script génère une valeur aléatoire (vous pouvez limiter la taille du nombre). L’utilisateur saisit une valeur. Le script informe l’utilisateur  : “plus” si le nombre généré est plus grand que celui saisi par l’utilisateur, “moins” si le nombre généré est inférieur. L’utilisateur doit trouver le nombre. Une fois le nombre trouvé, afficher une phrase de succès et quitter.    
**b.** Deuxième script : cette fois-ci, le script n'utilise plus votre console pour fonctionner :   
* plutôt que de saisir des nombres quand vous lancez le script, le script tournera en permanence, et vous utiliserez un fichier pour communiquer avec lui.
* il doit ouvrir un fichier (celui que vous voulez) et lire une valeur à l'intérieur (que vous avez écrit à la main)
* il doit remplacer le contenu du fichier par la réponse : "Plus grand" ou "Plus petit"
* à votre tour d'ouvrir le fichier et de tenter de deviner à nouveau

**c. Bonus** : écrire un script qui répond à votre place au jeu plus ou moins de la question b. Il doit afficher dans un fichier son nombre d'essai avant la bonne réponse, quelle était la bonne réponse ainsi que l'heure à laquelle il l'a trouvée.  

### 8. Sauvegarde de données 
Name : `8save`  

A l’aide de la commande `rsync`, effectuer la sauvegarde du répertoire `/home` dans le répertoire `/opt`.  
L’idée est d’archiver et compresser (`zip`, `tar.gz`, autres) le contenu de `/home`, et de copier l’archive obtenue dans `/opt`.   
Mettez en place un mécanisme permettant de ne garder que 5 sauvegardes. A la sixième sauvegarde, le script doit supprimer la première.  
Utilisez la `crontab` pour que ce script se lance tous les jours à midi.  

**Bonus** : utiliser un serveur de stockage pour les sauvegardes (deuxième VM). Dans le même script : 
* tester si le serveur de stockage distant est disponible
* s'il est disponible tester si une connexion SSH est possible
* si elle est possible, envoyer l'archie compressée à travers SSH sur le serveur distant
* si elle n'est pas possible : 
  * stocker la sauvegarde dans un répertoire dédié en local
  * envoyer toutes les sauvegardes une fois que le serveur est de nouveau disponible
  * une fois les sauvegardes locales copiées, le script doit les supprimer

### 9. Bonus : Ecrire un script permettant de générer des VirtualHost
Name : `9ggbro`

Bon je dis Virtual Host parce qu'on se fait comprendre simplement avec ce mot-là. C'est un mot lié au serveur web Apache, mais vous pouvez en utiliser un autre (vous gagnez des points en utilisant NGINX, comme ça, c'est gratuit, parce que ça me fait plaisir :) ).   

L'idée est la suivante : 
* le script va afficher des infos sur le serveur web actuellement installé
* il permettra à un utilisateur d'ajouter rapidement un site web en ne précisant qu'un minimum d'informations (port d'écoute et racine du site)

Pour ce faire : 
* votre script doit tester la présence d'Apache (ou du serveur web de votre choix), ainsi que son bon fonctionnement
* il doit afficher la version d'Apache installée
* il doit afficher une brève liste des VirtualHosts déjà configurés
  * bonus : il doit afficher s'ils sont configurés pour du HTTPS, et si oui, la date d'expiration de leur certificat
* si l'utilisateur le souhaite, il peut ajouter un VirtualHost grâce à une saisie interactive
  * l'utilisateur doit pouvoir choisir le port d'écoute
  * l'utilisateur doit pouvoir choisir la racine du site web
* le script doit générer une paire de clé/certificat (non signé) pour que le site fonctionne en HTTPS
* une fois terminé, le script affiche l'IP et le port où est joignable le nouveau site web 
* NB : votre firewall doit être activé, le bon port doit y être ajouté à chaque lancement :)
* NB2 : juste parce que c'est plus chiant ("plus compliqué à mettre en place et contraire aux bonnes prartiques"), et que je suis curieux de voir comment vous feriez ça (algorithmiquement parlant, avec les outils que vous propose le shell), vous devez mettre toute la configuration dans un seul fichier de conf. Si ça vous ennuie, faites une config propre, en ajoutant un fichier `.conf` par virtualhost dans `/etc/httpd/conf.d`
* **Bonus**-ception ? votre script gère la suppression de VirtualHost