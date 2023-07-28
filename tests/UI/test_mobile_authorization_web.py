import os

from dotenv import dotenv_values
from selene import browser, by, be, have


dotenv = dotenv_values()


def test_mobile_authorization_web(setup_browser, mobile_browser_management_web):
    browser.open('/')

    # WHEN
    browser.element('#cookie-alert-close button').click()
    browser.element('[class=h-btn__line]').click()
    browser.element('a[href="/account/"]').click()
    browser.element('[name=login]').type(f'{dotenv.get("login")}')
    browser.element('[name=password]').type(f'{dotenv.get("password")}')
    browser.element('[data-test=authFormSubmit]').click()
    # THEN
    browser.element('.lk-main-top__name').should(have.exact_text('Тест Даниил Тест'))
