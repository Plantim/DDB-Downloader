import requests #pour requête web
from platform   import system as system_name  # Returns the system/OS name
import os #permet d'utiliser des commandes, sert pour clear_screen

class Colored():

    def __init__(self, print_bool=True):
        self.have_to_print = print_bool
        self.green = "\033[1;32m"
        self.red = "\033[1;31m"
        self.end = "\033[0;0m"

    def PrintOn(self):
        self.have_to_print = True

    def PrintOff(self):
        self.have_to_print = False
        
    def OK(self, string):
        OK = "[" + self.green + "OK" + self.end + "] "
        if self.have_to_print:
            print(OK + string)
        return OK + string

    def ERROR(self, string):
        ERROR = "[" + self.red + "ERROR" + self.end + "] "
        if self.have_to_print:
            print(ERROR + string)
        return ERROR + string

#Vérifie l'entrée
def check_categorie(CAT):
    colored = Colored()
    categorie = input("Ecrire la catégorie à collecter ou 'all' pour toutes les récupérer : ")
    while categorie not in CAT and categorie != "all":
        os.system('cls' if system_name().lower()=='windows' else 'clear')
        colored.ERROR("La catégorie demandée n'est pas dans la liste ou est mal écrite.\n")
        print(*CAT, sep = ", ") #sépare les éléments avec des virgules
        print('\n')
        categorie = input("Ecrire la catégorie à collecter ou 'all' pour toutes les récupérer : ") #Demande la catégorie à extraire
    return categorie



#Télécharge les json de la catégorie
def download_json(url,nb_element_max,donnees):
    #Liste pour la fusion json
    #Téléchargement
    for i in range(50,nb_element_max,50):
        response = requests.get(url+str(i), allow_redirects=True) #requête en incrémentant 50 au skip
        #Concaténation de chaque requete dans la liste "donnees"
        donnees["data"] = donnees["data"]+response.json()["data"]
    donnees.pop("skip")
    donnees.pop("limit")
    return donnees

#affiche un message de fin
def message_fin(len_finaljson,categorie,compteur_all_categorie = 0):
    colored = Colored()
    colored.OK("L'opération s'est déroulée avec succès.")

    if compteur_all_categorie > 0: #Je regarde le compteur car s'il est utilisé, alors la fonction all est sélectionnée
        colored.OK(f"{compteur_all_categorie} fichiers json ont été créés dans le dossier output\n")
    else:
        colored.OK(f"Il y a {len_finaljson} éléments dans le fichier {categorie}.json !")

