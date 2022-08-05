#Author : Plantim
#BIG Contributor : Iooray
#Version : 1.0
#Description : Ce script télécharge la base de donnée de Dofusdb.fr


#import
import requests #pour requête web
import timeit
import os #pour créer un dossier + clear la fenêtre
import json #pour lire le json
import sys #permet de save dans le dossier output

import subprocess as sp #permet d'utiliser des commandes, sert pour clear_screen
from platform   import system as system_name  # Returns the system/OS name

#########################################################################################################################
####################################################   DEFINITIONS   ####################################################
#########################################################################################################################

#Efface l'écran peu importe l'OS
def clear_screen(): 
    if system_name().lower().startswith('win'):
        clear_the_screen = sp.call('cls', shell=True) # Windows <br>
    else:
        clear_the_screen = sp.call('clear', shell=True) # Linux

#Affiche la liste des catégories
def affiche_liste():
    #print(*liste_categorie, sep = "\n") #saute une ligne entre chaque élément
    global liste_categorie
    liste_categorie = ["achievements","achievement-categories","achievement-objectives","achievement-rewards","alignment-sides","almanax-calendars","areas","breeds","characteristics","challenges","companions","documents","dungeons","effects","emoticons","finish-moves","guild-rights","havenbag-themes","havenbag-furnitures","interactives","incarnation-informations","info-messages","items","item-sets","item-types","idols","idols-spell-levels","jobs","legendary-power-categories","living-object-skin-jnt-mood","legendary-treasure-hunts","map-positions","map-references","monsters","monster-races","monster-super-races","months","mounts","mount-behaviors","npcs","npc-messages","ornaments","point-of-interest","quests","quest-objectives","quest-steps","quest-objective-types","quest-step-rewards","random-drop-groups","recipes","servers","server-game-types","smiley-packs","spells","spell-levels","spell-states","spell-variants","spell-pairs","subareas","super-areas","skills","titles","worlds"]
    print(*liste_categorie, sep = ", ") #sépare les éléments avec des virgules
    print('\n')

#Demande la catégorie à extraire
def demande_categorie():
    global Categorie
    Categorie = input("Ecrire la catégorie à collecter ou 'all' pour toutes les récupérer : ")

#Vérifie l'entrée
def check_categorie():
    while Categorie not in liste_categorie and Categorie != "all":
        clear_screen()
        print("La catégorie demandée n'est pas dans la liste ou est mal écrite.\n")
        affiche_liste() #Affiche la liste des catégories
        demande_categorie() #Demande la catégorie à extraire

#reconstitue l'url
def reconstitue_url():
    global url
    url = "https://api.dofusdb.fr/" + Categorie + "?$limit=50&$skip="

#Détermine le nombre d'élément max dans la catégorie choisie
def determine_elements_max():
    global Nb_element_Max
    Nb_element_Max = requests.get(url).json()['total']

#Télécharge les json de la catégorie
def download_json():
    #Liste pour la fusion json
    global donnees
    donnees=[] 
    
    #Téléchargement
    for i in range(0,Nb_element_Max,50):
        requete = requests.get(url+str(i), allow_redirects=True) #requête en incrémentant 50 au skip
        
        #affiche la progression en pourcentage
        clear_screen()
        progression = round(i*100/Nb_element_Max,2)
        print(f"Catégorie {Categorie} extraite à : {progression} %\n")
        
        if compteur_all_categorie > 0: #Je regarde le compteur car s'il est utilisé, alors la fonction all est sélectionnée
            print(f"Catégorie : {compteur_all_categorie} sur {len(liste_categorie)}")

        end = timeit.default_timer()
        print(f"Temps écoulé : {round(end - start,2)}s\n")

        #Concaténation de chaque requete dans la liste "donnees"
        for key in requete.json()["data"]:
            donnees.append(key)

#Crée un dossier output s'il n'existe pas
def create_output_folder():
    global output_path
    output_path = "output"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

#fusionne tous les json
def fusion_json():
    global finaljson
    finaljson={}
    finaljson["total"]=Nb_element_Max
    finaljson["data"]=donnees

#sauvegarde le json fusionné dans le dossier output
def Save_json():
    f= open("%s.json" % (os.path.dirname(os.path.realpath(sys.argv[0]))+"/"+ output_path + "/" + Categorie),"w+")
    f.write("%s" % str(json.dumps(finaljson))) #json.dumps permet de renvoyer un json avec de vrais guillements
    f.close()

#affiche un message de fin
def Message_fin():
    clear_screen()
    print("L'opération s'est déroulée avec succès.\n")

    if compteur_all_categorie > 0: #Je regarde le compteur car s'il est utilisé, alors la fonction all est sélectionnée
        print(f"{compteur_all_categorie} fichiers json ont été créés dans le dossier output\n")
    else:
        print(f"Il y a {len(finaljson['data'])} éléments dans le fichier {Categorie}.json !\n")
    
    end = timeit.default_timer()
    print(f"L'extraction a pris {round(end - start,2)}s\n")
    print("Appuyez sur une touche pour quitter")
    input()


#########################################################################################################################
#####################################################   PROGRAMME   #####################################################
#########################################################################################################################

compteur_all_categorie = 0

affiche_liste() #Affiche la liste des catégories
demande_categorie() #Demande la catégorie à extraire
check_categorie() #Vérifie l'entrée

start = timeit.default_timer() #Demarre le timer

if Categorie in liste_categorie:
    reconstitue_url() #reconstitue l'url
    determine_elements_max() #Détermine le nombre d'élément max dans la catégorie choisie
    download_json() #Télécharge les json de la catégorie
    fusion_json() #fusionne tous les json
    create_output_folder() #Crée un dossier output s'il n'existe pas
    Save_json() #sauvegarde le json fusionné dans le dossier output
elif Categorie == "all":
    for i_categorie in liste_categorie:
        compteur_all_categorie += 1
        Categorie = i_categorie #Permet de faire varier la catégorie à chaque boucle
        reconstitue_url() #reconstitue l'url
        determine_elements_max() #Détermine le nombre d'élément max dans la catégorie choisie
        download_json() #Télécharge les json de la catégorie
        fusion_json() #fusionne tous les json
        create_output_folder() #Crée un dossier output s'il n'existe pas
        Save_json() #sauvegarde le json fusionné dans le dossier output

Message_fin() #affiche un message de fin