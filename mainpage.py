from basepage import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    url = 'http://prestashop-automation.qatestlab.com.ua/ru/'

    currency_dropdown                   =   [By.XPATH, '//*[@id="_desktop_currency_selector"]/div']
    currency_dropdown_value             =   [By.XPATH, '//*[@id="_desktop_currency_selector"]//*[contains(text(),\'']
    currency_dropdown_current_value     =   [By.XPATH, '//*[@id="_desktop_currency_selector"]/div/span[2]']
    product_cards_currency              =   [By.CLASS_NAME, 'price']
    product_cards                       =   [By.CLASS_NAME, 'thumbnail-container']
    total_search_products               =   [By.XPATH, '//*[@id="js-product-list-top"]/div[1]/p']
    search_input                        =   [By.XPATH, '//*[@id="search_widget"]/form/input[2]']
    submit_search_btn                   =   [By.XPATH, '//*[@id="search_widget"]/form/button/i']
    sort_dropdown                       =   [By.XPATH, '//*[@id="js-product-list-top"]/div[2]/div/div/a']
    sort_dropdown_value                 =   [By.XPATH, '//*[@class="row sort-by-row"]//*[contains(text(),\'']




    def search(self, value):
        self.input_elemnt(MainPage.search_input[0], MainPage.search_input[1], value)  # input text to search widget
        self.click_on_element(MainPage.submit_search_btn[0], MainPage.submit_search_btn[1])