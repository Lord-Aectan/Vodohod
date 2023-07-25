from selene import browser, by, be, have


def test_visible_price_table(desktop_browser_management_web):
    browser.open('https://vodohod.com/cruises/2024/teplohod-mustaj-karim-09-nov-13-nov-2024/')
    browser.element('#cookie-alert button').click()
    # WHEN
    browser.element('a[data-tab-btn="d-p_prices"]').click()

    # THEN
    browser.element('#vue-app-price-table').should(be.visible)
