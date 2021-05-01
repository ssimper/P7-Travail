from ..wiki_places import PAGEID, TITLE
from ..wiki_places import fake_data
from ..program.gps_wiki_request import RemarkablePlaces

def test_find_places_works(monkeypatch):
    class FakeResponse:
        def json(self):
            return fake_data

    def mock_request_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr('requests.get', mock_request_get)

    remarkable_places = RemarkablePlaces()
    list_places, dico_places, my_favorite_place_pageid, my_favorite_place_title = remarkable_places.find_places('tic', 'tac')
    assert my_favorite_place_pageid == PAGEID
    assert my_favorite_place_title == TITLE
