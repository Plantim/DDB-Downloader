import os 
from tqdm.asyncio import tqdm as tqdm_async

class Colored:
    def __init__(self, print_bool=True):
        self.have_to_print = print_bool
        self.green = "\033[1;32m"
        self.red = "\033[1;31m"
        self.end = "\033[0;0m"

    def print_on(self):
        self.have_to_print = True

    def print_off(self):
        self.have_to_print = False

    def ok(self, string):
        ok = f"[{self.green}OK{self.end}] "
        if self.have_to_print:
            print(ok + string)
        return ok + string

    def error(self, string):
        error = f"[{self.red}ERROR{self.end}] "
        if self.have_to_print:
            print(error + string)
        return error + string


def check_categorie(categories):
    colored = Colored()
    category = input("Enter the category to collect or 'all' to collect all: ")
    while category not in categories and category != "all":
        os.system('cls' if os.name == 'nt' else 'clear')
        colored.error("The requested category is not in the list or is misspelled.\n")
        print(', '.join(categories))
        print('\n')
        category = input("Enter the category to collect or 'all' to collect all: ")
    return category

#Télécharge les json de la catégorie
async def download_json_async(session, url, nb_element_max, donnees):
    for i in tqdm_async(range(50, nb_element_max, 50)):
        async with session.get(url + str(i)) as response:
            response_json = await response.json()
            donnees["data"] = donnees["data"] + response_json["data"]

    donnees.pop("skip")
    donnees.pop("limit")
    return donnees

#affiche un message de fin
def message_fin(len_finaljson, category, compteur_all_categorie=0):

    colored = Colored()
    colored.ok("The operation was successful.")

    if compteur_all_categorie > 0:
        colored.ok(f"{compteur_all_categorie} JSON files have been created in the output folder\n")
    else:
        colored.ok(f"There are {len_finaljson} items in the {category}.json file!")
    input()