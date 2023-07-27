import os
from selene import browser, by, be, have


def test_mobile_authorization_web(mobile_browser_management_web):
    login = os.getenv('login')
    password = os.getenv('password')
    browser.open('/')

    # WHEN
    browser.element('#cookie-alert-close button').click()
    browser.element('[class=h-btn__line]').click()
    browser.element('a[href="/account/"]').click()
    browser.element('[name=login]').type(f'{login}')
    browser.element('[name=password]').type(f'{password}')
    browser.element('[data-test=authFormSubmit]').click()
    # THEN
    browser.element('.lk-main-top__name').should(have.exact_text('Тест Даниил Тест'))
