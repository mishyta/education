from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    url = 'http://prestashop-automation.qatestlab.com.ua/ru/'

    currency_dropdown = [By.XPATH, '//*[@class="currency-selector dropdown js-dropdown"]']
    currency_dropdown_value = [By.XPATH, '//*[@id="_desktop_currency_selector"]//*[contains(text(),\'']
    currency_dropdown_current_value = [By.XPATH, '//*[@id="_desktop_currency_selector"]/div/span[2]']
    product_cards_currency = [By.XPATH, "//*[@class='thumbnail-container']//*[@class='price']"]
    product_cards = [By.XPATH, '//*[@class="thumbnail-container"]']
    product_price = [By.CLASS_NAME, 'price']
    product_regular_price = [By.CLASS_NAME, 'regular-price']
    product_discount = [By.CLASS_NAME, 'discount-percentage']
    total_search_products = [By.XPATH, '//*[@id="js-product-list-top"]/div[1]/p']
    search_input = [By.XPATH, '//*[@id="search_widget"]/form/input[2]']
    submit_search_btn = [By.XPATH, '//*[@id="search_widget"]/form/button/i']
    sort_dropdown = [By.XPATH, "//*[@class='select-title']"]
    sort_dropdown_value = [By.XPATH, '//*[@class="row sort-by-row"]//*[contains(text(),\'']

    def search(self, value):
        self.input_element(*MainPage.search_input, value)  # input text to search widget
        self.click_on_element(*MainPage.submit_search_btn)

    def get_regular_prices_of_goods(self):
        cards = self.get_elements(*MainPage.product_cards)
        prices_list = list()
        for card in cards:
            card = MainPage(card)
            try:
                card.driver.find_element(*MainPage.product_regular_price)
            except NoSuchElementException:
                prices_list.append(card.get_element_digit(*MainPage.product_price))
                continue
            prices_list.append(card.get_element_digit(*MainPage.product_regular_price))
        return prices_list

    def check_product_discount(self):
        if self.check_element_is(*MainPage.product_discount):
            assert (round((self.get_element_digit(*MainPage.product_regular_price) -
                           self.get_element_digit(*MainPage.product_price)) / self.get_element_digit(
                *MainPage.product_regular_price) * 100)) == \
                   self.get_element_digit(*MainPage.product_discount)

    def change_page_currency(self, value):
        self.click_on_element(*MainPage.currency_dropdown)
        self.change_dropdown_value(*MainPage.currency_dropdown_value, value)

    def sort_products(self, value):
        self.click_on_element(*MainPage.sort_dropdown)
        self.change_dropdown_value(*MainPage.sort_dropdown_value, value)
