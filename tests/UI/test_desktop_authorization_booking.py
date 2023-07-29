import allure
from allure_commons.types import Severity
from dotenv import dotenv_values
from selene import browser, by, be, have

dotenv = dotenv_values()


@allure.tag('booking')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на авторизацию')
@allure.title('Успешная авторизация с валидными данными в десктопной версии интерфейса booking')
def test_desktop_authorization_booking(setup_browser, desktop_browser_management_booking):
    with allure.step('Открываем интерфейс booking в браузере'):
        browser.open('/')

    # WHEN
    with allure.step('Нажимаем на Авторизоваться'):
        browser.element('[class^=header-top__btn]').click()
    with allure.step('Вводим логин'):
        browser.element('[id=auth_email]').click().type(f'{dotenv.get("login")}')
    with allure.step('Вводим пароль'):
        browser.element('[id=user_password]').click().type(f'{dotenv.get("password")}')
    with allure.step('Нажимаем Войти'):
        browser.element('.b-modal__bottom div').click()

    # THEN
    with allure.step('Авторизация прошла успешно и отображается ФИО: Тест Даниил Тест'):
        browser.element('.header-top__btn--auth span').should(have.exact_text('ТЕСТ ДАНИИЛ ТЕСТ'))
