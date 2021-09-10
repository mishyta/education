from _pytest.fixtures import fixture
import pytest
from mainpage import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


#fixture scope

@pytest.fixture  # Driver fixture
def driver():
    driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    yield driver
    driver.quit()





@pytest.mark.parametrize('value', ['UAH', 'EUR', 'USD'])
def test_currency_comparison(driver, value):  # 2
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.change_dropdown_value(MainPage.currency_dropdown[0], MainPage.currency_dropdown[1],
                                     MainPage.currency_dropdown_value[0], MainPage.currency_dropdown_value[1] + value + "')] ")
    assert page.get_element_text(page.currency_dropdown_current_value[0], page.currency_dropdown_current_value[1])[-1] \
           == page.get_element_text(page.product_cards_currency[0], page.product_cards_currency[1])[-1]


def test_total_search_products(driver):
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.search('dress')
    assert page.count_elements(page.product_cards[0], page.product_cards[1]) \
           == int(page.get_element_text(page.total_search_products[0], page.total_search_products[1])[-2])

@pytest.mark.parametrize('value', ['USD'])    # ['UAH', 'EUR', 'USD']
def test_check_product_cards_currency(driver,value):  # 6
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.search('dress')
    page.change_dropdown_value(MainPage.currency_dropdown[0], MainPage.currency_dropdown[1],
                               MainPage.currency_dropdown_value[0], MainPage.currency_dropdown_value[1] + value + "')] ")
    cards = page.get_elements_list(page.product_cards_currency[0], page.product_cards_currency[1])
    for card in cards:
        assert card.text[-1] == page.get_element_text(page.currency_dropdown_current_value[0], page.currency_dropdown_current_value[1])[-1]



