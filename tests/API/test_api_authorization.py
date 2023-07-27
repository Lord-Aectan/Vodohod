import logging
import os
from tests.API.helper import reqres_session


def test_authorization():
    login = os.getenv('login')
    password = os.getenv('password')
    response = reqres_session.post('/security/authorise',
                                   json={
                                       "login": f'{login}',
                                       "password": f'{password}'}
                                   )
    logging.info(response.json()['code'])
    assert response.status_code == 200
