import os
import allure
from dotenv import dotenv_values
from selene import browser, by, be, have
dotenv = dotenv_values()

def test_desktop_authorization_booking(setup_browser, desktop_browser_management_booking):
    with allure.step('Открываем браузер в интерфейсе booking'):
        browser.open('/')

    # WHEN
    with allure.step('Открываем форму авторизации'):
        browser.element('[class^=header-top__btn]').click()
    with allure.step('Вводим логин'):
        browser.element('[id=auth_email]').click().type(f'{dotenv.get("login")}')
    with allure.step('Вводим пароль'):
        browser.element('[id=user_password]').click().type(f'{dotenv.get("password")}')
    with allure.step('Нажимаем кнопку авторизации'):
        browser.element('.b-modal__bottom div').click()

    # THEN
    with allure.step('Проверяем, что авторизация прошла успешно и отображается наше ФИО'):
        browser.element('.header-top__btn--auth span').should(have.exact_text('ТЕСТ ДАНИИЛ ТЕСТ'))