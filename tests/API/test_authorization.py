import logging
import os
from dotenv import dotenv_values
from tests.API.helper import reqres_session
import allure
from allure_commons.types import Severity

dotenv = dotenv_values()


@allure.tag('API')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на авторизацию')
@allure.title('Авторизация с валидными данными в API')
def test_authorization():
    login = os.getenv('login')
    password = os.getenv('password')
    response = reqres_session.post('/security/authorise',
                                   json={
                                       "login": f'{dotenv.get("login")}',
                                       "password": f'{dotenv.get("password")}'}
                                   )
    logging.info(response.json()['code'])
    assert response.status_code == 200
