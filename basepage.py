from selenium import webdriver


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
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

    def change_dropdown_value(self, dropdown_locator, dropdown_locator_value, dropdown_value_locator,
                              dropdown_value_locator_value, value):
        self.click_on_element(dropdown_locator, dropdown_locator_value)  # open dropdown
        self.click_on_element(dropdown_value_locator,
                              dropdown_value_locator_value + value + "')] ")  # select dropdown value
