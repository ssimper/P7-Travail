FORMATED_ADDRESS = '42 Rue du Chevalier de la Barre, 75018'
LONGITUDE = 2.3431043
LATITUDE = 48.88670459999999
CONNECT_STATUS = 'OK'

fake_data = {'results': [{'address_components': [{'long_name': '35',
                                      'short_name': '35',
                                      'types': ['street_number']},
                                     {'long_name': 'Rue du Chevalier de la '
                                                   'Barre',
                                      'short_name': 'Rue du Chevalier de la '
                                                    'Barre',
                                      'types': ['route']},
                                     {'long_name': 'Paris',
                                      'short_name': 'Paris',
                                      'types': ['locality', 'political']},
                                     {'long_name': 'Département de Paris',
                                      'short_name': 'Département de Paris',
                                      'types': ['administrative_area_level_2',
                                                'political']},
                                     {'long_name': 'Île-de-France',
                                      'short_name': 'IDF',
                                      'types': ['administrative_area_level_1',
                                                'political']},
                                     {'long_name': 'France',
                                      'short_name': 'FR',
                                      'types': ['country', 'political']},
                                     {'long_name': '75018',
                                      'short_name': '75018',
                                      'types': ['postal_code']}],
              'formatted_address': FORMATED_ADDRESS,
              'geometry': {'location': {'lat': LATITUDE,
                                        'lng': LONGITUDE},
                           'location_type': 'ROOFTOP',
                           'viewport': {'northeast': {'lat': 48.88805358029149,
                                                      'lng': 2.344453280291502},
                                        'southwest': {'lat': 48.8853556197085,
                                                      'lng': 2.341755319708498}}},
              'place_id': 'ChIJ442GNENu5kcRGYUrvgqHw88',
              'plus_code': {'compound_code': 'V8PV+M6 Paris, France',
                            'global_code': '8FW4V8PV+M6'},
              'types': ['church',
                        'establishment',
                        'place_of_worship',
                        'point_of_interest',
                        'tourist_attraction']}],
 'status': CONNECT_STATUS}

