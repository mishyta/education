from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging



class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        logging.info('{}:open page with url:"{}".'.format(driver,url))

    def after_navigate_to(self, url, driver):

        logging.info('{}:page with url:"{}", opened.'.format(driver,url))

    def before_navigate_back(self, driver):
        logging.warning('not described: "before_navigate_back".')

    def after_navigate_back(self, driver):
        logging.warning('not described: "after_navigate_back".')

    def before_navigate_forward(self, driver):
        logging.warning('not described: "before_navigate_forward".')

    def after_navigate_forward(self, driver):
        logging.warning('not described: "after_navigate_forward".')

    def before_find(self, by, value, driver):
        logging.info('{}:find element with {} = "{}".'.format(driver,by,value))

    def after_find(self, by, value, driver):
        logging.info('{}:element with {} = "{}" selected.'.format(driver,by,value))

    def before_click(self, element, driver):
        logging.info('{}:click on ellement.'.format(driver))

    def after_click(self, element, driver):
        logging.info('{}:clicked'.format(driver))

    def before_change_value_of(self, element, driver):

        logging.info('{}:enter text in the selected item.'.format(driver))

    def after_change_value_of(self, element, driver):
        logging.info('{}:text entered.'.format(driver))

    def before_execute_script(self, script, driver):
        logging.warning('not described: "before_execute_script"')

    def after_execute_script(self, script, driver):
        logging.warning('not described: "after_execute_script"')

    def before_close(self, driver):
        logging.warning('not described: "before_close"')

    def after_close(self, driver):
        logging.warning('not described: "after_close"')

    def before_quit(self, driver):
        logging.info('{}:teardowning the driver.'.format(driver))

    def after_quit(self, driver):
        logging.info('{}:driver teardowned.'.format(driver))

    def on_exception(self, exception, driver):
        logging.info(('{}:on_exception: {}'.format(driver, exception))[:-1])

