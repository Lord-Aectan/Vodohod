import pprint
from dotenv import dotenv_values
from tests.API.helper import  reqres_session


def test_authorization():
    dotenv = dotenv_values()
    response = reqres_session.post('/security/authorise',
                             json={
                                 "login": f'{dotenv.get("login")}',
                                 "password": f'{dotenv.get("password")}'}
                             )
    pprint.pp(response.json())
    assert response.status_code == 200
