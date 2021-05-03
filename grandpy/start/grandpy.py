import random
from .sentences import welcome, thinking, response
from ..parser.program.parser01 import Parser
from ..google.program.google_request import GoogleDiscovery
from ..wikipedia.program.gps_wiki_request import RemarkablePlaces
from ..wikipedia.program.pageid_wiki_request import PlaceInformations

class InvocateGp:

    def the_question(self):
        grandpy_first_contact = random.choice(list(welcome.values()))
        grandpy_second_contact = random.choice(list(thinking.values()))
        print(grandpy_first_contact)
        question = input(
            "Quelle est ta question ?\nVotre question : "
            )
        print(grandpy_second_contact)
        return question

    def the_response(self, title, formatted_address, wiki_place_info, wiki_place_url):
        print("Alors voila, ", title," ce trouve à l'adresse ", formatted_address)
        print("et figure-toi que ", wiki_place_info)
        print("Mais si tu veux en savoir d'avantage, rends-toi à l'adresse ",
        wiki_place_url)


    def parser_job(self, to_parse):
        parser = Parser(to_parse)
        lowered = parser.lowerize()
        listed = parser.to_list()
        stopped = parser.check_stop_words()
        #print("Stopped = ", stopped)
        decodized = parser.decodize()
        ponc_removed = parser.remove_ponc()
        parsed_answer = ponc_removed
        #print(parsed_answer)
        return parsed_answer

    def google_job(self, answer):
        googlize = GoogleDiscovery()
        formatted_address, location_lat, location_lng, status = googlize.first_attempt(answer)
        return formatted_address, location_lat, location_lng

    def wikipedia_job(self, latitude, longitude):
        wiki_places = RemarkablePlaces()
        list_places, dico_places, my_favorite_place_pageid, my_favorite_place_title = wiki_places.find_places(latitude, longitude)
        places_info = PlaceInformations()
        # Collect detailed information and wiki url about the  place
        my_place_info, my_place_url = places_info.place_informations(
            my_favorite_place_pageid
            )
        # Create a dictionnary that contains key = name of the place and
        # value = the description of the place
        grandpy_third_contact = random.choice(list(response.values()))
        print(grandpy_third_contact)
        dico_places_info = {}
        for key, value in dico_places.items():
            new_value = places_info.place_informations(key)
            new_key = value
            dico_places_info[new_key] = new_value
        
        return my_favorite_place_title, my_place_info, my_place_url, dico_places_info
            




def main():
    
    test = InvocateGp()
    to_parse = test.the_question()
    parsed_question = test.parser_job(to_parse)
    google_address, google_lat, google_lng = test.google_job(parsed_question)
    wiki_title, wiki_place_info, wiki_place_url, wiki_dico_places_info = test.wikipedia_job(google_lat, google_lng)
    test.the_response(wiki_title, google_address, wiki_place_info, wiki_place_url)
    
    
    


if __name__ == "__main__":
    main()

