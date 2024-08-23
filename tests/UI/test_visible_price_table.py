from selene import browser, by, be, have
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'dmoiseenko')
@allure.feature('Задачи на доступность бронирования')
@allure.title('Не авторизованному пользователю доступна Таблица цен')
def test_visible_price_table(setup_browser, desktop_browser_management_web):
    with allure.step('Открываем страницу круиза'):
        browser.open('/cruises/2025/teplohod-konstantin-korotkov-04-nov-07-nov-2025/')
    with allure.step('Закрываем окно про куки'):
        browser.element('#cookie-alert button').click()
    # WHEN
    with allure.step('В списке меню нажимаем Цены и переходим к таблице цен'):
        browser.element('a[data-tab-btn="d-p_prices"]').click()

    # THEN
    with allure.step('Проверяем наличие таблицы цен'):
        browser.element('#vue-app-price-table').should(be.visible)
