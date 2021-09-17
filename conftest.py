import logging
import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
import allure
import subprocess

ALLURE_REPORT_DIR = 'allure-results'

logging.basicConfig(filename='webdriver.log', level=logging.INFO, format='[%(levelname)s][%(asctime)s]:%(message)s')
open('webdriver.log', 'w').close()


def pytest_configure(config):
    config.option.allure_report_dir = ALLURE_REPORT_DIR
    config.option.clean_alluredir = True


def pytest_sessionfinish():
    subprocess.check_output(['allure', 'generate', '--clean'], shell=True)



@pytest.fixture()  # Driver fixture
def driver():
    with allure.step('Driver init'):
        driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    yield driver
    with allure.step('driver teardown'):
        driver.quit()



