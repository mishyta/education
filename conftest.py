import logging
import pytest
from selenium import webdriver
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from allure_commons.types import AttachmentType
import allure

BROWSERS_FOR_TESTS = ["chrome", "firefox", "opera"]
LOGGING_FILE = 'webdriver.log'
COMMAND_EXECUTOR = "http://10.8.0.99:4444/wd/hub"
ALLURE_RESULTS_DIR = 'allure-results'
SELENOID_OPTIONS = {
    "enableVNC": True,
    "enableVideo": True
}
logging.basicConfig(
    filename=LOGGING_FILE,
    level=logging.INFO,
    format='[%(levelname)s][%(asctime)s]:%(message)s'
)

capabilities_ff = {
    "browserName": "firefox",
    "browserVersion": "92.0",
    "selenoid:options": SELENOID_OPTIONS
}

capabilities_chrome = {
    "browserName": "chrome",
    "browserVersion": "93.0",
    "selenoid:options": SELENOID_OPTIONS
}

capabilities_opera = {
    "browserName": "opera",
    "browserVersion": "79.0",
    "selenoid:options": SELENOID_OPTIONS
}


def pytest_configure(config):
    open(LOGGING_FILE, 'w').close()
    config.option.allure_report_dir = ALLURE_RESULTS_DIR
    config.option.clean_alluredir = False

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(params=BROWSERS_FOR_TESTS)  # Driver fixture
def driver(request):
    if request.param == "chrome":
        capabilities = capabilities_chrome
    elif request.param == "firefox":
        capabilities = capabilities_ff
    elif request.param == "opera":
        capabilities = capabilities_opera
    else:
        print('{} not supported.'.format(request.param))
    with allure.step(
            'Init with capabilities: {}:{}'.format(capabilities['browserName'], capabilities['browserVersion'])):
        driver = webdriver.Remote(command_executor=COMMAND_EXECUTOR, desired_capabilities=capabilities)
        driver = EventFiringWebDriver(driver, MyListener())
        driver.implicitly_wait(10)
        driver.maximize_window()
    yield driver
    with allure.step('Driver teardown.'):
        if request.node.rep_call.failed:
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        driver.quit()

