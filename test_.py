
import subprocess
import pytest
from mainpage import MainPage, ProductCard # as MP
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import allure
from contextlib import contextmanager


# @contextmanager
# def file_open(path):
#
#     try:
#         log = open(path, 'w')
#         yield log
#     finally:
#         log.close()
#
# with file_open('webdriver.log') as log:
#     log.write('')




@allure.feature('Test mainpage')
@allure.story('test_1')
@pytest.mark.parametrize('value', ['UAH', 'EUR', 'USD'])
def test_currency_comparison(driver, value):  # 2
    page = MainPage(driver)
    page.open_page(page.url)
    page.change_page_currency(value)
    assert page.get_element_text(*page.currency_dropdown_current_value)[-1] == \
           page.get_element_text(*ProductCard.currency)[-1]

@allure.feature('Test mainpage')
@allure.story('test_2')
def test_total_search_products(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    assert page.count_elements(*ProductCard.locator) == int(page.get_element_text(*page.total_search_products)[-2])

@allure.feature('Test mainpage')
@allure.story('test_3')
@pytest.mark.parametrize('value', ['USD'])  # ['UAH', 'EUR', 'USD']
def test_check_product_cards_currency(driver, value):  # 6
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    page.change_page_currency(value)
    cards = page.get_elements_list(*ProductCard.currency)
    for card in cards:
        assert card.text[-1] == page.get_element_text(*page.currency_dropdown_current_value)[-1]

@allure.feature('Test mainpage')
@allure.story('test_4')
def test_check_sort_price_high_to_low(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    prices_list_to_the_discount = page.get_list_with_regular_prices()
    page.sort_products('Цене: от высокой к низкой')
    prices_list_after_the_discount = page.get_list_with_regular_prices()
    assert sorted(prices_list_to_the_discount)[::-1] == prices_list_after_the_discount

@allure.feature('Test mainpage')
@allure.story('test_5')
def test_check_products_with_discount_contains_values(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    cards = page.get_elements(*ProductCard.locator)
    for card in cards:
        card = ProductCard(card)
        if card.check_element_is(*card.discount):
            assert card.get_element_text(*card.discount)[-1] == '%'
            assert card.check_element_is(*card.regular_price)

@allure.feature('Test mainpage')
@allure.story('test_6')
def test_check_product_matching_discount(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    cards = page.get_elements(*ProductCard.locator)
    for card in cards:
        card = ProductCard(card)
        if card.check_element_is(*card.discount):
            card.check_product_discount()


