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


def test_1_open_login_page(driver):
    page = MainPage(driver)
    page.open_page(MainPage.url)


@pytest.mark.parametrize('value', ['UAH', 'EUR', 'USD'])
def test_2_currency_comparison(driver, value):
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.change_page_currency(value)
    assert page.get_element_text(page.currency_dropdown_current_value[0], page.currency_dropdown_current_value[1])[-1] \
           == page.get_element_text(page.goods_currency[0], page.goods_currency[1])[-1]


def test_3_change_currency_to_value(driver):
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.change_page_currency('USD')  # values = 'USD', 'EUR', 'UAH'


def test_4_test_search(driver):
    page = MainPage(driver)
    page.open_page(MainPage.url)
    page.search('dress')  # input text to search
