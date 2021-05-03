from pprint import pprint
import requests
from ..wiki_places import fake_data

class PlaceInformations:

    def place_informations(self, page_id):
        
        """variables definition"""
        url = "https://fr.wikipedia.org/w/api.php"
        #page_id = fake_data['query']['geosearch'][0]['pageid']

        """parameters"""
        params = {
            "format": "json", # format de la réponse
            "action": "query", # action à effectuer
            "prop": "extracts|info", # Choix des propriétés pour les pages requises
            "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
            "exchars": 1200, # Nombre de caractères à retourner
            "explaintext": True, # Renvoyer du texte brut (éliminer les balises de markup)
            "pageids": page_id
        }

        response = requests.get(url, params=params)

        extracts_data = response.json()
        #print("Voici la réponse obtenue: ")
        #pprint(extracts_data)
        wanted_data = extracts_data['query']['pages'][str(page_id)]['extract']
        wanted_url = extracts_data['query']['pages'][str(page_id)]['fullurl']
        return wanted_data, wanted_url


def main():
    places = PlaceInformations(page_id)



if __name__ == "__main__":
    main()