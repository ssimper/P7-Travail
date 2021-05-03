from pprint import pprint
import requests



class RemarkablePlaces:

    def find_places(self, latitude, longitude):

        """variables definition"""
        url = "https://fr.wikipedia.org/w/api.php"
        list_places = []
        dico_places = {}

        """parameters"""
        params = {
            "format": "json", # format de la réponse
            "action": "query", # action à réaliser
            "list": "geosearch", # méthode de recherche
            "gsradius": 10000, # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gscoord": f"{latitude}|{longitude}", # coordonnées GPS séparées par une barre verticale
        }

        response = requests.get(url, params=params)
        geosearch_data = response.json()
        # I want all places (i put them in a dictionary)
        # the key is the pageid and the value is the title.
        list_places = geosearch_data['query']['geosearch']
        for element in list_places:
            dico_places[element['pageid']] = element['title']
        # But my favorite place is 'Basilique du Sacré-Cœur de Montmartre'
        my_favorite_place_pageid = geosearch_data['query']['geosearch'][0]['pageid']
        my_favorite_place_title = geosearch_data['query']['geosearch'][0]['title']
        

        return list_places, dico_places, my_favorite_place_pageid, my_favorite_place_title


def main():
    places = RemarkablePlaces()
    list_places, dico_places, my_favorite_place_pageid, my_favorite_place_title = places.find_places(48.88670459999999, 2.3431043)
    pprint(list_places)
    pprint(dico_places)
    for key, value in dico_places.items():
        print(f"Pageid n°{key}, lieu remarquable : {value}")


if __name__ == "__main__":
    main()
#latitude = 48.88670459999999
#longitude = 2.3431043
 


