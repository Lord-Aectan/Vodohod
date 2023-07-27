import logging
from dotenv import dotenv_values
from tests.API.helper import  reqres_session
import pprint

def test_authorization():
    dotenv = dotenv_values()
    response = reqres_session.post('/security/authorise',
                             json={
                                 "login": f'{dotenv.get("login")}',
                                 "password": f'{dotenv.get("password")}'}
                             )
    logging.info(response.json()['code'])
    assert response.status_code == 200
