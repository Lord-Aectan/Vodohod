import pprint
from tests.API.helper import reqres_session
import allure
from allure_commons.types import Severity


@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на отображение информации по круизам')
@allure.title('Если круиза не существует, то вернётся \'Круиз не найден\'')
def test_cruise_with_incorrect_id_is_not_on_the_site():
    response = reqres_session.get('/ru/cruises/one/84848')
    pprint.pp(response.json())
    assert response.status_code == 400
    assert response. json()['error']['error_msg'] == 'Круиз не найден'
