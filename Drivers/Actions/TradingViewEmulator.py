from selenium import webdriver
import selenium.webdriver.firefox.webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_firefox_options() -> Options:
    options = Options()
    options.headless = False
    return options


def get_firefox_web_driver(options: Options):
    return webdriver.Firefox(options=options)


def open_url_in_driver(url: str, web_driver: selenium.webdriver.firefox.webdriver.WebDriver) \
        -> selenium.webdriver.firefox.webdriver.WebDriver:
    web_driver.get(url)
    return web_driver


def emulate_loading_all_stocks_in_trading_view(web_driver: selenium.webdriver.firefox.webdriver.WebDriver) -> str:
    try:
        web_driver.find_element(By.CLASS_NAME, "loadButton-SFwfC2e0").click()
    except NoSuchElementException:
        return web_driver.page_source
    return emulate_loading_all_stocks_in_trading_view(web_driver)
