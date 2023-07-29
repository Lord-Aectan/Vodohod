from allure_commons.types import Severity
import allure
from dotenv import dotenv_values
from selene import browser, by, be, have


dotenv = dotenv_values()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на авторизацию')
@allure.title('Успешная авторизация с валидными данными в мобильной версии сайта')
def test_mobile_authorization_web(setup_browser, mobile_browser_management_web):
    with allure.step('Открываем сайт'):
        browser.open('/')

    # WHEN
    with allure.step('Закрываем окно про куки'):
        browser.element('#cookie-alert-close button').click()
    with allure.step('Нажимаем на сэндвич-меню'):
        browser.element('[class=h-btn__line]').click()
    with allure.step('Нажимаем на Войти в личный кабинет'):
        browser.element('a[href="/account/"]').click()
    with allure.step('Вводим логин'):
        browser.element('[name=login]').type(f'{dotenv.get("login")}')
    with allure.step('Ввдоим пароль'):
        browser.element('[name=password]').type(f'{dotenv.get("password")}')
    with allure.step('Нажимаем на Войти'):
        browser.element('[data-test=authFormSubmit]').click()
    # THEN
    with allure.step('Авторизация прошла успешно и загрузилась страница ЛК с ФИО: Тест Даниил Тест'):
        browser.element('.lk-main-top__name').should(have.exact_text('Тест Даниил Тест'))
