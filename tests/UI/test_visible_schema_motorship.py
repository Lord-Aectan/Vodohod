from selene import browser, by, be, have
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на проверку корректности схемы')
@allure.title('У т/х Мустай Карим загружена и отображается схема теплохода')
def test_visible_schema_motorship(setup_browser, desktop_browser_management_web):
    with allure.step('Открываем сайт'):
        browser.open('/')
    with allure.step('Закрываем окно про куки'):
        browser.element('#cookie-alert button').click()

    # WHEN
    with allure.step('Открываем меню со списком теплоходов'):
        browser.element('a[href="/ships/"]').hover()
    with allure.step('Выбираем т/х Мустай Карим и открываем его'):
        browser.element('a[href="/ships/mustai-karim/"]').click()
    with allure.step('Открываем схему теплохода'):
        browser.element('.ship-gallery__scheme-image').click()

    # THEN
    with allure.step('Схема теплохода открылась'):
        browser.element('.fancybox-image').should(be.visible)
