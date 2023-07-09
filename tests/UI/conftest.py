import pytest
from selene import browser

@pytest.fixture
def browser_management(scope='function'):
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.config.base_url = 'https://vodohod.com/'
    browser.config.timeout = 10
    yield

    browser.quit()