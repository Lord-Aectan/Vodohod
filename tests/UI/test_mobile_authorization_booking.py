from dotenv import dotenv_values
from selene import browser, by, be, have


def test_mobile_authorization_booking(mobile_browser_management_booking):
    login = os.getenv('login')
    password = os.getenv('password')
    browser.open('/')

    # WHEN
    browser.element('.header-top__btn--auth').click()
    browser.element('#auth_email').type(f'{login}')
    browser.element('#user_password').type(f'{password}')
    browser.element('.b-modal__bottom div').click()

    # THEN
    browser.element('.header-top__group--btn .def').should(have.text('ТЕСТ ДАНИИЛ ТЕСТ'))
