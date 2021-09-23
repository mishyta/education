import logging
import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from allure_commons.types import AttachmentType
import allure




LOGGING_FILE = 'webdriver.log'
open(LOGGING_FILE, 'w').close()

logging.basicConfig(
    filename=LOGGING_FILE,
    level=logging.INFO,
    format='[%(levelname)s][%(asctime)s]:%(message)s'
)

open(LOGGING_FILE, 'w').close()

command_executor = "http://10.8.0.99:4444/wd/hub"

capabilities = {
    "browserName": "firefox",
    "browserVersion": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

def pytest_configure(config):
    config.option.allure_report_dir = 'allure-results'
    config.option.clean_alluredir = True


@pytest.fixture()  # Driver fixture
def driver():
    with allure.step('Init with capabilities: {}:{}'.format(capabilities['browserName'],capabilities['browserVersion'])):
        driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=capabilities)
        driver = EventFiringWebDriver(driver,MyListener())
        driver.implicitly_wait(0.3)
    yield driver
    with allure.step('Driver teardown.'):
        allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        driver.quit()



