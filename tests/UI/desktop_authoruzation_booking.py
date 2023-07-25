from dotenv import dotenv_values
from selene import browser, by, be, have


def test_authorization_bookinkg(desktop_browser_management_booking):
    dotenv = dotenv_values()

    browser.open('/')

    # WHEN
    browser.element('[class^=header-top__btn]').click()
    browser.element('[id=auth_email]').click().type(f'{dotenv.get("login")}')
    browser.element('[id=user_password]').click().type(f'{dotenv.get("password")}')
    browser.element('.b-modal__bottom div').click()

    # THEN
    browser.element('.header-top__btn--auth span').should(have.exact_text('ТЕСТ ДАНИИЛ ТЕСТ'))
