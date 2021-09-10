from _pytest.fixtures import fixture
import pytest
from mainpage import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


@pytest.fixture  # Driver fixture
def driver():
    driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    yield driver
    driver.quit()


def test_open_login_page(driver):  # 1
    page = MainPage(driver)
    page.open_page(MainPage.url)


@pytest.mark.parametrize('value', ['UAH', 'EUR', 'USD'])
def test_currency_comparison(driver, value):  # 2
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.change_page_currency(value)
    assert page.get_element_text(page.currency_dropdown_current_value[0], page.currency_dropdown_current_value[1])[-1] \
           == page.get_element_text(page.product_cards_currency[0], page.product_cards_currency[1])[-1]


def test_change_currency_to_value(driver):  # 3
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.change_page_currency('USD')  # values = 'USD', 'EUR', 'UAH'


def test_search(driver):  # 4
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.search('dress')  # input text to search


def test_total_search_products(driver):  # 5
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.search('dress')
    assert page.count_elements(page.product_cards[0], page.product_cards[1]) \
           == int(page.get_element_text(page.total_search_products[0], page.total_search_products[1])[-2])


def test_check_product_cards_currency(driver):  # 6
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.search('dress')
    cards = page.get_elements_list(page.product_cards_currency[0], page.product_cards_currency[1])
    for card in cards:
        assert card.text[-1] == page.get_element_text(page.currency_dropdown_current_value[0], page.currency_dropdown_current_value[1])[-1]


def test_click_on_sort_dropdown(driver):
    pass