import requests
from platform   import system as system_name
import os
from tqdm import tqdm

class Colored():
    """Sert à ajouter de la couleur"""
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

def check_categorie(CAT_E,CAT_S):
    """Vérifie l'entrée de la catégorie"""
    colored = Colored()
    categorie = input("2 options :\n- Ecrire la catégorie à collecter.\n- Ecrire 'all_endpoints' ou 'all_supertypes' pour récupérer toutes les catégories associées.\n\nChoix : ")
    while categorie not in CAT_E and categorie not in CAT_S and categorie != "all_endpoints" and categorie != "all_supertypes":
        os.system('cls' if system_name().lower()=='windows' else 'clear')
        colored.ERROR("La catégorie demandée n'est pas dans la liste ou est mal écrite.\n")
        print(*CAT_E, sep = ", ")
        print('\n')
        print(*CAT_S, sep = ", ")
        print('\n')
        categorie = input("2 options :\n- Ecrire la catégorie à collecter.\n- Ecrire 'all_endpoints' ou 'all_supertypes' pour récupérer toutes les catégories associées.\n\nChoix : ")
    return categorie

def download_json(url,nb_element_max,donnees,categorie):
    """Télécharge les json de la catégorie"""
    for i in tqdm(range(50,nb_element_max,50), desc=categorie, leave=False): #commence à 50 car une 1er requête à 0 a été effectuée pour recup le nb_elem_max
        response = requests.get(url+str(i), allow_redirects=True) 
        donnees["data"] = donnees["data"]+response.json()["data"] #Concaténation de chaque requete dans la liste "donnees"
    donnees.pop("skip")
    donnees.pop("limit")
    return donnees


def message_fin(len_finaljson,categorie,compteur_all_categorie = 0):
    """affiche un message de fin"""
    colored = Colored()
    colored.OK("L'opération s'est déroulée avec succès.")

    if compteur_all_categorie > 0: #Je regarde le compteur car s'il est utilisé, alors la fonction all est sélectionnée
        colored.OK(f"{compteur_all_categorie} fichiers json ont été créés dans le dossier output\n")
    else:
        colored.OK(f"Il y a {len_finaljson} éléments dans le fichier {categorie}.json !")

def check_recommencer():
    """Vérifie s'il faut recommencer le programme"""
    colored = Colored()
    recommencer = input("\nRécupérer une autre catégorie ? (y/n) : ")
    while recommencer != "y" and recommencer != "n":
        os.system('cls' if system_name().lower()=='windows' else 'clear')
        colored.ERROR("L'entrée n'est pas correcte.\n")
        recommencer = input("Récupérer une autre catégorie ? (y/n) : ") 
    return recommencer