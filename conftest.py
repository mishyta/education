import logging
import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver





LOGGING_FILE = 'webdriver.log'


logging.basicConfig(
    filename=LOGGING_FILE,
    level=logging.INFO,
    format='[%(levelname)s][%(asctime)s]:%(message)s'
)

open(LOGGING_FILE, 'w').close()







@pytest.fixture()  # Driver fixture
def driver():
    driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    driver.maximize_window()
    yield driver
    driver.quit()



