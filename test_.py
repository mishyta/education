import logging

import pytest
from mainpage import MainPage, ProductCard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from listen import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import allure



@allure.story('test_currency_comparison')
@pytest.mark.parametrize('currency', ['UAH', 'EUR','USD'])
def test_currency_comparison(driver, currency):  # 2
    page = MainPage(driver)
    page.open_page(page.url)
    page.change_page_currency(currency)
    with allure.step('Perform verification that the price of products in the'
                     ' "Popular Products" section is indicated in accordance '
                     'with the installed currency in the header of the site (USD, EUR, UAH). '.format(currency)):
        assert page.get_element_text(*page.currency_dropdown_current_value)[-1] == \
               page.get_element_text(*ProductCard.currency)[-1]

@allure.story('test_total_search_products')
@pytest.mark.parametrize('currency', ['USD'])  # ['UAH', 'EUR', 'USD']
def test_total_search_products(driver, currency):
    page = MainPage(driver)
    page.open_page(page.url)
    page.change_page_currency(currency)
    page.search('dress')
    with allure.step('Take the check that the page "Search results" contains the inscription '
                     '"Goods: X", where X is the number of truly found items. '):
        assert page.count_elements(*ProductCard.locator) == int(page.get_element_text(*page.total_search_products)[-2])


@allure.story('test_check_product_cards_currency')
@pytest.mark.parametrize('currency', ['USD'])  # ['UAH', 'EUR', 'USD']
def test_check_product_cards_currency(driver, currency):  # 6
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    page.change_page_currency(currency)
    with allure.step('Check that the price of all the results shown is displayed in dollars. '):
        cards = page.get_elements_list(*ProductCard.currency)
        for card in cards:
            assert card.text[-1] == page.get_element_text(*page.currency_dropdown_current_value)[-1]


@allure.story('test_check_sort_price_high_to_low')
def test_check_sort_price_high_to_low(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    prices_list_to_the_discount = page.get_list_with_regular_prices()
    page.sort_products('Цене: от высокой к низкой')
    with allure.step('Check that goods are sorted by price, while some goods can be at a discount, '
                     'and the price is used during sorting. '):
        prices_list_after_the_discount = page.get_list_with_regular_prices()
        assert sorted(prices_list_to_the_discount)[::-1] == prices_list_after_the_discount


@allure.story('test_check_products_with_discount_contains_values')
def test_check_products_with_discount_contains_values(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    cards = page.get_elements(*ProductCard.locator)
    with allure.step('For discount products, a percentage discount is indicated along with the price before and '
                     'after the discount.  '):
        page.driver.implicitly_wait(0)
        for card in cards:
            card = ProductCard(card)
            if card.check_element_is(*card.discount):
                assert card.get_element_text(*card.discount)[-1] == '%'
                assert card.check_element_is(*card.regular_price)


@allure.story('test_check_product_matching_discount')
def test_check_product_matching_discount(driver):
    page = MainPage(driver)
    page.open_page(page.url)
    page.search('dress')
    with allure.step('Check that the price before and after the discount coincides with the specified discount size. '):
        cards = page.get_elements(*ProductCard.locator)
        page.driver.implicitly_wait(0)
        for card in cards:
            card = ProductCard(card)
            if card.check_element_is(*card.discount):
                card.check_product_discount()

