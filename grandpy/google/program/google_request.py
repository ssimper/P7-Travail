import requests
from pprint import pprint
from ...credentials import google_key


class GoogleDiscovery:


    def first_attempt(self, search):
        
        """Variables definition"""
        url = "https://maps.googleapis.com/maps/api/geocode/json?"

        """Parameters"""
        payload = {
            #"address": "3 allee de l euro ezanville,+FR",
            "address": search,
            "key": google_key
        }

        res = requests.get(url, params=payload)
        output = res.json()
        #pprint(output)
        formatted_address = output['results'][0]['formatted_address']
        location_lat = output['results'][0]['geometry']['location']['lat']
        location_lng = output['results'][0]['geometry']['location']['lng']
        status = output['status']
        return formatted_address, location_lat, location_lng, status


def main():

    test = GoogleDiscovery()
    formatted_address, location_lat, location_lng, status = test.first_attempt("sacré coeur, Paris")
    print(status, formatted_address, location_lat, location_lng)
    


if __name__ == "__main__":
    main()
