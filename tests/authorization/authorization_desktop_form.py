from selene import browser, have, command
import os
import allure

login = os.getenv('login')
password = os.getenv('password')


class AuthorizationDesktopForm:
    def open(self):
        with allure.step('Открываем сайт'):
            browser.open('/')

    def close_coockie_alert(self):
        with allure.step('Закрываем окно про куки'):
            browser.element('#cookie-alert button').click()

    def open_authorization_form(self):
        with allure.step('Открываем форму авторизации'):
            browser.element('.h__lk').click()

    def type_login(self):
        with allure.step('Вводим логин'):
            browser.element('[name=login]').type(f'{login}')

    def type_password(self):
        with allure.step('Ввдоим пароль и жмём Enter'):
            browser.element('[name=password]').type(f'{password}').press_enter()

    def should_have_authorization(self, value):
        with allure.step('Проверяем, что авторизация прошла успешно и отображается наше ФИО'):
            browser.element('[class=h__lk-text]').should(have.text(f'{value}'))
