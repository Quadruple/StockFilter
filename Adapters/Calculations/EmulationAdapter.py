import selenium.webdriver.firefox.webdriver
from selenium.webdriver.firefox.options import Options
from Drivers.Actions.TradingViewEmulator import get_firefox_options, get_firefox_web_driver, \
    open_url_in_firefox_driver, emulate_loading_all_stocks_in_trading_view
from Drivers.Data.WebScrapingData import trading_view_url, index_to_analyze, index_name_prefix


def get_url_to_scrape_components() -> str:
    return trading_view_url.replace(index_name_prefix, index_to_analyze)


def get_browser_options() -> Options:
    return get_firefox_options()


def get_web_driver(options: Options) -> selenium.webdriver.firefox.webdriver.WebDriver:
    return get_firefox_web_driver(options)


def open_url_in_driver(url: str, web_driver: selenium.webdriver.firefox.webdriver.WebDriver) -> \
        selenium.webdriver.firefox.webdriver.WebDriver:
    return open_url_in_firefox_driver(url, web_driver)


def emulate_click_on_load_more_button(web_driver: selenium.webdriver.firefox.webdriver.WebDriver) -> str:
    return emulate_loading_all_stocks_in_trading_view(web_driver)
