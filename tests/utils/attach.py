import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_log_browser(browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(body=log, name='browsers_logs', attachment_type=AttachmentType.TEXT, extension='.log')
