import allure
from allure_commons.types import Severity
from dotenv import dotenv_values
from selene import browser, by, be, have

dotenv = dotenv_values()



@allure.tag('booking')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на авторизацию')
@allure.title('Успешная авторизация с валидными данными в мобильной версии интерфейса booking')
def test_mobile_authorization_booking(setup_browser, mobile_browser_management_booking):
    with allure.step('Открываем интерфейс booking в браузере'):
        browser.open('/')

    # WHEN
    with allure.step('Нажимаем на Авторизоваться'):
        browser.element('.header-top__btn--auth').click()
    with allure.step('Вводим логин'):
        browser.element('#auth_email').type(f'{dotenv.get("login")}')
    with allure.step('Вводим пароль'):
        browser.element('#user_password').type(f'{dotenv.get("password")}')
    with allure.step('Нажимаем Войти'):
        browser.element('.b-modal__bottom div').click()

    # THEN
    with allure.step('Авторизация прошла успешно и отображается ФИО: Тест Даниил Тест'):
        browser.element('.header-top__group--btn .def').should(have.text('ТЕСТ ДАНИИЛ ТЕСТ'))
