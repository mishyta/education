import logging
import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import allure




LOGGING_FILE = 'webdriver.log'


logging.basicConfig(
    filename=LOGGING_FILE,
    level=logging.INFO,
    format='[%(levelname)s][%(asctime)s]:%(message)s'
)

open(LOGGING_FILE, 'w').close()







@pytest.fixture()  # Driver fixture
def driver():
    driver = webdriver.Remote(command_executor='http://10.8.0.99:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    # driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    driver.implicitly_wait(0.3)
    yield driver
    driver.quit()



