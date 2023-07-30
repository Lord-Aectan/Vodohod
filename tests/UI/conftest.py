import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv, dotenv_values

from utils import attach

dotenv = dotenv_values()

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv('../.env')


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.add_argument('--disable-dev-shm-usage')

    options.capabilities.update(selenoid_capabilities)

    # login = os.getenv('SELENOID_LOGIN')
    # password = os.getenv('SELENOID_PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{dotenv.get("SELENOID_LOGIN")}:{dotenv.get("SELENOID_PASSWORD")}'
                         f'@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver
    print('Connection with Selenoid: OK')


@pytest.fixture
def desktop_browser_management_web():
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.config.base_url = 'https://vodohod.com'
    browser.config.timeout = 10

    yield

    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture
def mobile_browser_management_web():
    browser.config.window_width = 375
    browser.config.window_height = 667
    browser.config.base_url = 'https://vodohod.com/'
    browser.config.timeout = 10

    yield

    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture
def desktop_browser_management_booking():
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.config.base_url = 'https://booking.vodohod.com/?lang=ru&cruise_id=16823'
    browser.config.timeout = 10

    yield

    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture
def mobile_browser_management_booking():
    browser.config.window_width = 495
    browser.config.window_height = 667
    browser.config.base_url = 'https://booking.vodohod.com/?lang=ru&cruise_id=16823'
    browser.config.timeout = 10

    yield

    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()
