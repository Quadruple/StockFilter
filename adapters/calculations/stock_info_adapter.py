"""
This module provides abstraction for fetching component data.
The received data contains features like Close Prices, Open Prices, Volume etc.
"""
import pandas as pd
import yfinance as yf
from drivers.calculations.stock_info_fetcher import get_stock_from_yahoo, \
    get_stock_data_from_yahoo


def get_stock(stock_name: str) -> yf.Ticker:
    """ Abstraction of getting the stock. Currently YahooFinance is used. """
    return get_stock_from_yahoo(stock_name)


def get_stock_data(
        ticker: yf.Ticker, interval: str, start_date: str, end_date: str
) -> pd.DataFrame:
    """ Abstraction of getting historical data of a stock. """
    return get_stock_data_from_yahoo(ticker, interval, start_date, end_date)
