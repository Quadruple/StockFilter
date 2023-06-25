"""
This module is an abstraction for web scraping and formatting between different data sources.
"""
from drivers.calculations.index_searcher import scrape_stocks_from_trading_view
from drivers.actions.stock_formatter import transform_stock_names_into_yahoo_format


def scrape_component_names_under_index(page_source: str) -> list[str]:
    """ Abstraction for web scraping operation. Currently TradingView is scraped. """
    return scrape_stocks_from_trading_view(page_source)


def transform_stock_names(stocks: list[str]) -> list[str]:
    """
    Abstraction for transforming stock names.
    Currently, stock names obtained from TradingView does not match Yahoo Finance stocks.
    For compatibility between TradingView and YahooFinance, stock names are transformed.
    """
    return transform_stock_names_into_yahoo_format(stocks)
