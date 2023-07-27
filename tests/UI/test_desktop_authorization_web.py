from tests.authorization.authorization_desktop_form import AuthorizationDesktopForm


def test_authorization_form_web(desktop_browser_management_web):
    authorization_desktop_form = AuthorizationDesktopForm()
    # WHEN
    authorization_desktop_form.open()
    authorization_desktop_form.close_coockie_alert()
    authorization_desktop_form.open_authorization_form()
    authorization_desktop_form.type_login()
    authorization_desktop_form.type_password()

    # THEN
    authorization_desktop_form.should_have_authorization('Даниил Тест')