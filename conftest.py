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

capabilities_ff = {
    "browserName": "firefox",
    "browserVersion": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

capabilities_chrome = {
    "browserName": "chrome",
    "browserVersion": "93.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

capabilities_opera = {
    "browserName": "opera",
    "browserVersion": "79.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

def pytest_configure(config):
    config.option.allure_report_dir = 'allure-results'
    config.option.clean_alluredir = True


# @pytest.fixture # Driver fixture
# def driver():
#     with allure.step('Init with capabilities: {}:{}'.format(capabilities['browserName'],capabilities['browserVersion'])):
#         driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=capabilities_ff)
#         driver = EventFiringWebDriver(driver,MyListener())
#         driver.implicitly_wait(0.3)
#         driver.maximize_window()
#     yield driver
#     with allure.step('Driver teardown.'):
#         allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
#         driver.quit()

@pytest.fixture(params=["chrome", "firefox", "opera"]) # Driver fixture
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=capabilities_chrome)
    if request.param == "firefox":
        driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=capabilities_ff)
    if request.param == "opera":
        driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=capabilities_opera)
    driver.implicitly_wait(10)
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    driver.quit()

