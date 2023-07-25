import pytest
from selene import browser


@pytest.fixture
def desktop_browser_management_web():
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.config.base_url = 'https://vodohod.com/'
    browser.config.timeout = 10
    yield

    browser.quit()


@pytest.fixture
def mobile_browser_management_web():
    browser.config.window_width = 375
    browser.config.window_height = 667
    browser.config.base_url = 'https://vodohod.com/'
    browser.config.timeout = 10
    yield

    browser.quit()

@pytest.fixture
def desktop_browser_management_booking():
        browser.config.window_width = 1500
        browser.config.window_height = 1200
        browser.config.base_url = 'https://booking.vodohod.com/?lang=ru&cruise_id=16823'
        browser.config.timeout = 10
        yield

        browser.quit()

@pytest.fixture
def mobile_browser_management_booking():
            browser.config.window_width = 495
            browser.config.window_height = 667
            browser.config.base_url = 'https://booking.vodohod.com/?lang=ru&cruise_id=16823'
            browser.config.timeout = 10
            yield

            browser.quit()
