# DDB-Downloader
Script python pour télécharger la base de donnée de [Dofusdb.fr](https://dofusdb.fr/)

## Pré-requis

Installer les librairies "requests" et "tqdm"

### Utilisateur Windows :
- Lancer l'invite de commandes (touche Windows + R)
- Ecrire "cmd"
- Ecrire `pip install requests`
  - S'il est indiqué : `pip' n'est pas reconnu en tant que commande interne ou externe, un programme exécutable ou un fichier de commandes`
  - Il faudra installer la dernière version de python3 depuis le Microsoft Store 
- Ecrire `pip install tqdm`

### Utilisateur MacOS :
- Installer python3 depuis le site : [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Ouvrir le terminal (Commande ⌘ + Espace, et écrire "terminal" ; ou depuis le launchpad puis écrire "terminal" dans la barre de recherche)
- Ecrire `pip install requests`
- Ecrire `pip install tqdm`


## Utilisation

Démarer le main.py

2 options :
- Entrer le nom d'une catégorie présente dans l'une des listes (ci-dessous)
- Entrer "all_endpoints" ou "all_supertypes" pour télécharger tous les éléments de la catégorie correspondante.

## Fonctionnement

Le script téléchargera tous les fichiers json liés à la catégorie puis les compilera pour n'en former qu'un.

Les fichiers json seront enregistrés dans le dossier "output" (modifiable dans le config.ini) qui sera créé dans le même répertoire que le script !

## Liste des catégories prises en charge

### Liste des Endpoints
- achievements
- achievement-categories
- achievement-objectives
- achievement-rewards
- alignment-sides
- almanax-calendars
- areas
- breeds
- characteristics
- challenges
- companions
- documents
- dungeons
- effects
- emoticons
- finish-moves
- guild-rights
- havenbag-themes
- havenbag-furnitures
- interactives
- incarnation-informations
- info-messages
- items
- item-sets
- item-types
- idols
- idols-spell-levels
- jobs
- legendary-power-categories
- living-object-skin-jnt-mood
- legendary-treasure-hunts
- map-positions
- map-references
- monsters
- monster-races
- monster-super-races
- months
- mounts
- mount-behaviors
- npcs
- npc-messages
- ornaments
- point-of-interest
- quests
- quest-objectives
- quest-steps
- quest-objective-types
- quest-step-rewards
- random-drop-groups
- recipes
- servers
- server-game-types
- smiley-packs
- spells
- spell-levels
- spell-states
- spell-variants
- spell-pairs
- subareas
- super-areas
- skills
- titles
- worlds

### Liste des Supertypes
- amulette
- arme
- anneau
- ceinture
- bottes
- consommable
- bouclier
- ressource
- chapeau
- cape
- montilier_familier
- dofus_spot
- event_quete
- mutation
- nouriture_boost
- benediction
- malediction
- rp_buff
- suiveur
- apparat
- compagnon
- harnachement
- costume
- monture
