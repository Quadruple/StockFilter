"""
This module is an abstraction to firing up a web browser in background for web scraping.
Some websites like TradingView have hidden data under their "Load More" / "Show More" buttons.
This module emulates clicking on those buttons to make sure that all data is available for scraping.
"""
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from Drivers.Actions.TradingViewEmulator import get_firefox_options, get_firefox_web_driver, \
    open_url_in_firefox_driver, emulate_loading_all_stocks_in_trading_view
from Drivers.Data.WebScrapingData import trading_view_url, index_to_analyze, index_name_prefix


def get_url_to_scrape_components() -> str:
    """ Abstraction to get proper url of the website for web scraping component names. """
    return trading_view_url.replace(index_name_prefix, index_to_analyze)


def get_browser_options() -> Options:
    """ Abstraction to get options for the web driver used by selenium. """
    return get_firefox_options()


def get_web_driver(options: Options) -> WebDriver:
    """ Abstraction to get the web driver with the provided options. """
    return get_firefox_web_driver(options)


def open_url_in_driver(url: str, web_driver: WebDriver) -> WebDriver:
    """ Abstraction to open url to scrape using the selenium web driver. """
    return open_url_in_firefox_driver(url, web_driver)


def emulate_click_on_load_more_button(web_driver: WebDriver) -> str:
    """ Abstraction for clicking load more button to make all data available for scraping. """
    return emulate_loading_all_stocks_in_trading_view(web_driver)
