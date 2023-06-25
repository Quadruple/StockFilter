"""
This module provides abstraction for fetching component data.
The received data contains features like Close Prices, Open Prices, Volume etc.
"""
import pandas as pd
import yfinance as yf
from drivers.calculations.StockInfoFetcher import get_stock_from_yahoo, \
    get_daily_stock_data_from_yahoo


def get_stock(stock_name: str) -> yf.Ticker:
    """ Abstraction of getting the stock. Currently YahooFinance is used. """
    return get_stock_from_yahoo(stock_name)


def get_daily_stock_data(ticker: yf.Ticker, year_span: int) -> pd.DataFrame:
    """ Abstraction of getting daily data of a stock. Contains features like Close/Open Prices. """
    return get_daily_stock_data_from_yahoo(ticker, year_span)
