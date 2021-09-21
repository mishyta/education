import logging
import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities





LOGGING_FILE = 'webdriver.log'


logging.basicConfig(
    filename=LOGGING_FILE,
    level=logging.INFO,
    format='[%(levelname)s][%(asctime)s]:%(message)s'
)

open(LOGGING_FILE, 'w').close()







@pytest.fixture()  # Driver fixture
def driver():
    # driver = EventFiringWebDriver(webdriver.Remote(command_executor='http://10.8.0.99:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX), MyListener())
    driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()



