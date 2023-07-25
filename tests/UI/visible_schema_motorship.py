from selene import browser, by, be, have


def test_visible_schema_motorship(desktop_browser_management_web):
    browser.open('/')
    browser.element('#cookie-alert button').click()

    # WHEN
    browser.element('a[href="/ships/"]').hover()
    browser.element('a[href="/ships/mustai-karim/"]').click()
    browser.element('.ship-gallery__scheme-image').click()

    # THEN
    browser.element('.fancybox-image').should(be.visible)
