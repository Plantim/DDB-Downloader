# DDB-Downloader
Script python pour télécharger la base de donnée de Dofusdb.fr

## Pré-requis

Installer la librairie "requests" et "tqdm"

### Utilisateur Windows :
- Lancer l'invite de commande (touche Windows + R)
- Ecrire "cmd"
- Ecrire "pip install requests"
- Ecrire "pip install tqdm"

- s'il est indiqué : 'pip' n'est pas reconnu en tant que commande interne ou externe, un programme exécutable ou un fichier de commandes.
- Il faudra installer python, 
- Ecrire "python"
- Une fenêtre microsoft store s'ouvre, cliquer sur "installer"
- une fois installé, recommencer les étapes précédentes


### Utilisateur MacOS :
- installer python normalement depuis le site : https://www.python.org/ftp/python/3.10.6/python-3.10.6-macos11.pkg
- Ecrire "pip install request"
- Ecrire "pip install tqdm"


## Utilisation

Entrez le nom d'une catégorie présente dans la liste (ci-dessous) ou écrivez "all" pour toutes les télécharger.

## Fonctionnement

Le script téléchargera tous les fichiers json liés à la catégorie puis les compilera pour n'en former qu'un.

Les fichiers json seront enregistrés dans le dossier "output" qui sera créé dans le même répertoire que le script !

## Liste

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
