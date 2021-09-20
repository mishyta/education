from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from decimal import Decimal
import re
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        with allure.step('Open page:'+url):
            self.driver.get(url)

    def get_element_text(self, locator, value):
        return self.driver.find_element(locator, value).text

    def click_on_element(self, locator, value):
        self.driver.find_element(locator, value).click()

    def input_element(self, locator, value, text):
        self.driver.find_element(locator, value).send_keys(text)

    def search_elements(self, locator, value):
        return self.driver.find_elements(locator, value)

    def count_elements(self, locator, value):
        return len(self.driver.find_elements(locator, value))

    def get_elements_list(self, locator, value):
        return self.driver.find_elements(locator, value)

    def get_elements(self, locator, value):
        return self.driver.find_elements(locator, value)

    def change_dropdown_value(self, dropdown_value_locator, dropdown_value_locator_value, value):
        self.click_on_element(dropdown_value_locator,
                              dropdown_value_locator_value + value + "')] ")  # select dropdown value
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((dropdown_value_locator, dropdown_value_locator_value + value + "')] "),
                                             value))

    def check_element_is(self, locator, value):
        try:
            self.driver.find_element(locator, value)
        except NoSuchElementException:
            return False
        return True

    def get_element_digit(self, locator, value):
        price = self.driver.find_element(locator, value).text
        price = re.sub('\D', '', price)
        return int(price)

    def get_element_digit_(self, locator, value):
        price = self.driver.find_element(locator, value).text
        price = ''.join(filter(str.isdigit, price))
        return int(price)
