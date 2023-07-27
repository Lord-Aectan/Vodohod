import pytest
import os
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome")
    parser.addoption('--browser_version', action='store', default="99.0")


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_chrome(request):
    browser_name = request.config.getoption('browser_name')
    browser_version = request.config.getoption('browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": f"{browser_name}",
        "browserVersion": f"{browser_version}",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    yield

    browser.quit()

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

