import pprint
from tests.API.helper import reqres_session
import allure
from allure_commons.types import Severity


@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на отображение информации по круизам')
@allure.title('При запросе существующего круиза по нему возвращается информация')
def test_included_cruise_available_on_site():
    response = reqres_session.get('/ru/cruises/one/19036')
    pprint.pp(response.json())
    assert response.status_code == 200
