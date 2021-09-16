import logging

import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
import allure
import subprocess

logging.basicConfig(filename='webdriver.log',level=logging.INFO)

def pytest_configure(config):

    config.option.allure_report_dir = 'D:\\tasks\\1\\allure-results'
    config.option.clean_alluredir = True

@pytest.fixture(scope='session',autouse=True)
def allure_generate():
    yield
    subprocess.check_output(['allure', 'generate','--clean'], shell=True)





@pytest.fixture()  # Driver fixture
def driver():
    driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    with allure.step('Driver init'):
         pass
    yield driver
    driver.quit()
    with allure.step('driver teardown'):
         pass