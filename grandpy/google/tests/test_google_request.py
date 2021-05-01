from ..data import FORMATED_ADDRESS, LATITUDE, LONGITUDE, CONNECT_STATUS
from ..data import fake_data
from ..program.google_request import GoogleDiscovery

def test_first_attempt_works(monkeypatch):
    class FakeResponse:
        def json(self):
            return fake_data

    def mock_request_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr('requests.get', mock_request_get)

    google_discovery = GoogleDiscovery()
    address, latitude, longitude, connect_status = google_discovery.first_attempt('gkjdlkfgjdlkj')
    assert address == FORMATED_ADDRESS
    assert latitude == LATITUDE
    assert longitude == LONGITUDE
    assert connect_status == CONNECT_STATUS

