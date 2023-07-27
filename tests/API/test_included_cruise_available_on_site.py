import pprint
from tests.API.helper import  reqres_session


def test_included_cruise_available_on_site():
    response =reqres_session.get('/ru/cruises/one/17799')
    pprint.pp(response.json())
    assert response.status_code == 200
