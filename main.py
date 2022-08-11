#Author : Plantim
#Contributors : Iooray, Cleaver
#Version : 1.3
#Description : Ce script télécharge la base de données de Dofusdb.fr

import json
import sys
import configparser
from utils import *
from tqdm import tqdm

#Lis des variables dans le fichier config
config = configparser.ConfigParser()
config.read('config.ini')
CAT_E = config['dofusdb.fr']['endpoints'].split(',')
CAT_S = config['dofusdb.fr']['supertypes'].split(',')
output_path = config['DEFAULT']['output_path']
categorie = config['DEFAULT']['categorie']


def run(categorie):
    """Fonction principale"""
    #Forme l'url
    if (categorie in CAT_S):
        url = config['supertype'][categorie]
        url = url.replace("&$skip=0","",1) #pourrait être supprimé en formattant les url dans le fichier config
        url = url + "&$limit=50" + "&$skip="
    if (categorie in CAT_E):
        url = "https://api.dofusdb.fr/" + categorie + "?$limit=50&$skip="
     
    donnees = requests.get(url).json()
    nb_element_max = donnees["total"]
    finaljson = download_json(url,nb_element_max,donnees,categorie)
    
    #Crée un dossier output s'il n'existe pas
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    #Crée le fichier .json
    f=open("%s.json" % (os.path.dirname(os.path.realpath(sys.argv[0]))+"/"+ output_path + "/" + categorie),"w+")
    f.write("%s" % str(json.dumps(finaljson))) #json.dumps permet de renvoyer un json avec de vrais guillements
    f.close()
    return len(finaljson['data'])


if __name__ == '__main__':
    
    recommencer = "none"
    while recommencer != "n":
        if (categorie in CAT_E) or (categorie == "all_endpoints") or (categorie in CAT_S) or (categorie == "all_supertypes"): #skip le input manuel si la catégorie est préconfigurée dans config
            pass
        else:
            categorie = check_categorie(CAT_E,CAT_S) #input manuel

        #action en fonction de la catégorie
        if categorie == "all_endpoints":
            for i_categorie in tqdm(range(len(CAT_E)), desc=categorie):
                len_finaljson = run(CAT_E[i_categorie])
            message_fin(len_finaljson,categorie,len(CAT_E))
        elif categorie == "all_supertypes":
            for i_categorie in tqdm(range(len(CAT_S)), desc=categorie):
                len_finaljson = run(CAT_S[i_categorie])
            message_fin(len_finaljson,categorie,len(CAT_S))
        else:
            message_fin(run(categorie),categorie)

        recommencer = check_recommencer()
        if recommencer == "y": 
            os.system('cls' if system_name().lower()=='windows' else 'clear')
            categorie = "none"