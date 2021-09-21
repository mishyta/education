from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from decimal import Decimal, ROUND_HALF_UP



class MainPage(BasePage):
    url = 'http://prestashop-automation.qatestlab.com.ua/ru/'

    currency_dropdown = [By.XPATH, '//*[@class="currency-selector dropdown js-dropdown"]']
    currency_dropdown_value = [By.XPATH, '//*[@id="_desktop_currency_selector"]//*[contains(text(),\'']
    currency_dropdown_current_value = [By.XPATH, '//*[@id="_desktop_currency_selector"]/div/span[2]']
    total_search_products = [By.XPATH, '//*[@id="js-product-list-top"]/div[1]/p']
    search_input = [By.XPATH, '//*[@id="search_widget"]/form/input[2]']
    submit_search_btn = [By.XPATH, '//*[@id="search_widget"]/form/button/i']
    sort_dropdown = [By.XPATH, "//*[@class='select-title']"]
    sort_dropdown_value = [By.XPATH, '//*[@class="row sort-by-row"]//*[contains(text(),\'']

    def search(self, value):

        self.input_element(*MainPage.search_input, value)  # input text to search widget
        self.click_on_element(*MainPage.submit_search_btn)

    def get_list_with_regular_prices(self):
        cards = self.get_elements(*ProductCard.locator)
        prices_list = list()
        for card in cards:
            card = ProductCard(card)
            try:
                card.driver.find_element(*card.regular_price)
            except NoSuchElementException:
                prices_list.append(card.get_element_digit(*card.price))
                continue
            prices_list.append(card.get_element_digit(*card.regular_price))
        return prices_list

    def change_page_currency(self, value):

        self.click_on_element(*MainPage.currency_dropdown)
        self.change_dropdown_value(*MainPage.currency_dropdown_value, value)

    def sort_products(self, value):

        self.click_on_element(*MainPage.sort_dropdown)
        self.change_dropdown_value(*MainPage.sort_dropdown_value, value)


class ProductCard(BasePage):
    locator = [By.XPATH, '//*[@class="thumbnail-container"]']
    currency = [By.XPATH, "//*[@class='thumbnail-container']//*[@class='price']"]
    price = [By.CLASS_NAME, 'price']
    regular_price = [By.CLASS_NAME, 'regular-price']
    discount = [By.CLASS_NAME, 'discount-percentage']

    def check_product_discount(self):
        disc = (self.get_element_digit(*ProductCard.regular_price) - self.get_element_digit(
            *ProductCard.price)) / self.get_element_digit(*ProductCard.regular_price)
        disc = Decimal(disc)
        disc = disc.quantize(Decimal("1.00"), ROUND_HALF_UP) * 100
        assert disc == self.get_element_digit(*ProductCard.discount)
