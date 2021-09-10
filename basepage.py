from selenium import webdriver


class BasePage():


    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element_text(self, lokator, value):
        return self.driver.find_element(lokator, value).text

    def click_on_element(self, lokator, value):
        self.driver.find_element(lokator, value).click()

    def input_elemnt(self, lokator, value, text):
        self.driver.find_element(lokator, value).send_keys(text)

    def search_elements(self, lokator, value):
        return self.driver.find_elements(lokator, value)

    def count_elements(self, lokator, value):
        return len(self.driver.find_elements(lokator, value))

    def get_elements_list(self, lokator, value):
        return self.driver.find_elements(lokator, value)


