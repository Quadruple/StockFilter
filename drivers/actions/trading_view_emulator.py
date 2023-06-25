"""
This module is an extension from emulation adapter.
It emulates connecting to the TradingView website using the FireFox web browser
and fetches needed data from TradingView by web scraping as well as emulates clicking
on "Show More" buttons to so that all data can be scraped.
"""
from selenium import webdriver
import selenium.webdriver.firefox.webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_firefox_options() -> Options:
    """
    Function for preparing the options of FireFox web browser
    which will be used by Selenium module. Currently the only option
    is the headless mode which takes the FireFox browser to the background.
    """
    options = Options()
    options.headless = True
    return options


def get_firefox_web_driver(options: Options) -> selenium.webdriver.firefox.webdriver.WebDriver:
    """ Function for preparing a FireFox web driver. """
    return webdriver.Firefox(options=options)


def open_url_in_firefox_driver(
    url: str, web_driver: selenium.webdriver.firefox.webdriver.WebDriver
) -> selenium.webdriver.firefox.webdriver.WebDriver:
    """ Function for opening the given URL in the given Firefox Browser. """
    web_driver.get(url)
    return web_driver


def emulate_loading_all_stocks_in_trading_view(
    web_driver: selenium.webdriver.firefox.webdriver.WebDriver
) -> str:
    """
    For some stock indexes or countries, TradingView screen does not load all the stocks.
    The hidden data cannot be web scraped. In order to make the hidden data visible,
    "Show More" button should be clicked. This function clicks that button until it disappears and
    makes sure that there are no hidden data.
    """
    try:
        web_driver.find_element(By.CLASS_NAME, "loadButton-SFwfC2e0").click()
    except NoSuchElementException:
        return web_driver.page_source
    return emulate_loading_all_stocks_in_trading_view(web_driver)
