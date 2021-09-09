from basepage import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    url = 'http://prestashop-automation.qatestlab.com.ua/ru/'

    currency_dropdown                   =   [By.XPATH, '//*[@id="_desktop_currency_selector"]/div']
    currency_dropdown_usd               =   [By.XPATH, '//*[@id="_desktop_currency_selector"]/div/ul/li[3]/a']
    currency_dropdown_uah               =   [By.XPATH, '//*[@id="_desktop_currency_selector"]/div/ul/li[2]/a']
    currency_dropdown_eur               =   [By.XPATH, '//*[@id="_desktop_currency_selector"]/div/ul/li[1]/a']
    currency_dropdown_current_value     =   [By.XPATH, '//*[@id="_desktop_currency_selector"]/div/span[2]']
    goods_currency                      =   [By.XPATH, '//*[@id="content"]/section/div/article[1]/div/div[1]/div/span']
    search_input                        =   [By.XPATH, '//*[@id="search_widget"]/form/input[2]']
    submit_search_btn                   =   [By.XPATH, '//*[@id="search_widget"]/form/button/i']

    def change_page_currency(self, value):
        self.click_on_element(MainPage.currency_dropdown[0], MainPage.currency_dropdown[1])
        if value == 'USD':
            self.click_on_element(MainPage.currency_dropdown_usd[0],MainPage.currency_dropdown_usd[1])
        elif value == 'EUR':
            self.click_on_element(MainPage.currency_dropdown_eur[0],MainPage.currency_dropdown_eur[1])
        elif value == 'UAH':
            self.click_on_element(MainPage.currency_dropdown_uah[0],MainPage.currency_dropdown_uah[1])
        else:
            pass

    def search(self, value):
        self.input_elemnt(MainPage.search_input[0], MainPage.search_input[1], value)  # input text to search widget
        self.click_on_element(MainPage.submit_search_btn[0], MainPage.submit_search_btn[1])