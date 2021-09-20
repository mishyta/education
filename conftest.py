import logging
import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
import allure
import subprocess
from allure_commons.types import AttachmentType



ALLURE_RESULTS_DIR = 'allure-results'
ALLURE_RESULTS_DIR_AUTOCLEAN = False
AllURE_GENERATE_CMD = ['allure', 'generate', '--clean']
LOGGING_FILE = 'webdriver.log'


logging.basicConfig(
    filename=LOGGING_FILE,
    level=logging.INFO,
    format='[%(levelname)s][%(asctime)s]:%(message)s'
)

open(LOGGING_FILE, 'w').close()


def pytest_configure(config):
    config.option.allure_report_dir = ALLURE_RESULTS_DIR
    config.option.clean_alluredir = ALLURE_RESULTS_DIR_AUTOCLEAN


def pytest_sessionfinish():
    subprocess.check_output(AllURE_GENERATE_CMD, shell=True)



@pytest.fixture()  # Driver fixture
def driver():
    with allure.step('Driver init'):
        driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
        driver.maximize_window()
    yield driver
    with allure.step('driver teardown'):
        allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        driver.quit()



