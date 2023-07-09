import os
from dotenv import dotenv_values
from selene import browser, by, be, have


def test_authorization_form_web(browser_management):
    dotenv = dotenv_values()
    # WHEN
    browser.open('/')
    browser.element('.h__lk').click()
    browser.element('[name=login]').type(f'{dotenv.get("login")}')
    browser.element('[name=password]').type(f'{dotenv.get("password")}').press_enter()

    # THEN
    browser.element('[class=h__lk-text]').should(have.text('Даниил Тест'))
