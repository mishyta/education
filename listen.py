from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


test_log = open('webdriver.log', 'a')

class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print(driver, ':', "open page:", '"' + url + '"', file=test_log)

    def after_navigate_to(self, url, driver):
        print(driver, ':', 'page' + '" ' + url + '"' + ' opened', file=test_log)

    def before_navigate_back(self, driver):
        print("before navigating back ", driver.current_url)

    def after_navigate_back(self, driver):
        print("After navigating back ", driver.current_url)

    def before_navigate_forward(self, driver):
        print("before navigating forward ", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After navigating forward ", driver.current_url)

    def before_find(self, by, value, driver):
        print(driver, ':', "driver find element with", by, ' = ' + '"' + value + '"', file=test_log)

    def after_find(self, by, value, driver):
        print(driver, ':', 'element with ', by, ' = ' + '"' + value + '"', 'selected', file=test_log)

    def before_click(self, element, driver):
        print(driver, ':', 'click on selected element ^', file=test_log)

    def after_click(self, element, driver):
        print(driver, ':', "clicked", file=test_log)

    def before_change_value_of(self, element, driver):
        print(driver, ':', "input text in selected element ", file=test_log)

    def after_change_value_of(self, element, driver):
        print(driver, ':', "text entered ", file=test_log)

    def before_execute_script(self, script, driver):
        print("before_execute_script")

    def after_execute_script(self, script, driver):
        print("after_execute_script")

    def before_close(self, driver):
        print(driver, ':', "close driver", file=test_log)

    def after_close(self, driver):
        print(driver, ':', 'closed!', file=test_log)

    def before_quit(self, driver):
        print(driver, ':', "close driver", file=test_log)

    def after_quit(self, driver):
        print(driver, ':', "closed!", file=test_log)

    def on_exception(self, exception, driver):
        print("on_exception")
