from _pytest.fixtures import fixture
import pytest
from mainpage import MainPage # as MP
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


# fixture scope  для ініціалізації файла в який лістенер буде записувати дії драйвера

test_log = open('webdriver.log', 'w')



@pytest.fixture  # Driver fixture
def driver():
    driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    yield driver
    driver.quit()


@pytest.mark.parametrize('value', ['UAH', 'EUR', 'USD'])
def dtest_currency_comparison(driver, value):  # 2
    page = MainPage(driver)
    page.open_page(page.url)
    page.change_page_curency(value)
    assert page.get_element_text(*page.currency_dropdown_current_value)[-1] == \
           page.get_element_text(*page.product_cards_currency)[-1]


def dtest_total_search_products(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    assert page.count_elements(*page.product_cards) == int(page.get_element_text(*page.total_search_products)[-2])


@pytest.mark.parametrize('value', ['USD'])  # ['UAH', 'EUR', 'USD']
def dtest_check_product_cards_currency(driver, value):  # 6
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    page.change_page_curency(value)
    cards = page.get_elements_list(*page.product_cards_currency)
    for card in cards:
        assert card.text[-1] == page.get_element_text(*page.currency_dropdown_current_value)[-1]

def dtest_check_sort_price_high_to_low(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    prices_list_to_the_discount = page.get_regular_prices_of_goods()
    page.sort_products('Цене: от высокой к низкой')
    prices_list_after_the_discount = page.get_regular_prices_of_goods()
    assert sorted(prices_list_to_the_discount)[::-1] == prices_list_after_the_discount

def dtest_check_products_with_discount_contains_values(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    cards = page.get_elements(*page.product_cards)
    for card in cards:
        card = MainPage(card)
        if card.check_element_is(*card.product_discount) == True:
            assert card.get_element_text(*card.product_discount)[-1] == '%'
            assert card.check_element_is(*card.product_regular_price) == True

def dtest_check_product_matching_discount(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    cards = page.get_elements(*page.product_cards)
    for card in cards:
        card = MainPage(card)
        if card.check_element_is(*card.product_discount) == True:
            card.check_product_discount()

