#Author : Plantim
#BIG Contributor : Iooray
#Version : 1.0
#Description : Ce script télécharge la base de donnée de Dofusdb.fr

import json
import sys
import configparser
from ast import literal_eval
from utils import * #permet de faire des opérations sur les fichiers

config = configparser.ConfigParser()
config.read('config.ini')
CAT = config['dofusdb.fr']['categories'].split(',') #Liste des catégories
output_path = config['DEFAULT']['output_path'] #Chemin du dossier output
categorie = config['DEFAULT']['categorie'] #Catégorie à extraire


def run(categorie):
    url = "https://api.dofusdb.fr/" + categorie + "?$limit=50&$skip=" #reconstitue l'url
    nb_element_max = requests.get(url).json()['total'] #Détermine le nombre d'élément max dans la catégorie choisie
    donnees = download_json(url,nb_element_max) #Télécharge les json de la catégorie
    finaljson = fusion_json(nb_element_max,donnees) #fusionne tous les json
    #Crée un dossier output s'il n'existe pas
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    f=open("%s.json" % (os.path.dirname(os.path.realpath(sys.argv[0]))+"/"+ output_path + "/" + categorie),"w+")
    f.write("%s" % str(json.dumps(finaljson))) #json.dumps permet de renvoyer un json avec de vrais guillements
    f.close()
    return len(finaljson['data'])

if __name__ == '__main__':
    if (categorie in CAT) or (categorie == "all"): #Vérifie si la catégorie est dans la liste
        pass
    else:
        categorie = check_categorie(CAT) #input manuel
    if categorie != "all":
        len_finaljson = run(categorie)        
        message_fin(len_finaljson,categorie) #affiche un message de fin
    else:
        for i_categorie in tqdm(range(len(CAT))):
            len_finaljson = run(CAT[i_categorie])
        message_fin(len_finaljson,categorie,len(CAT)) #affiche un message de fin
        