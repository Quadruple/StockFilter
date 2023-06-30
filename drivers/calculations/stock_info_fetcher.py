"""
This module is an extension to stock info adapter.
Its responsibility is to provide functionalities on Yahoo Finance API
such as fetching a stocks data.
"""
import yfinance as yf
import pandas as pd


def get_stock_from_yahoo(stock_name: str) -> yf.Ticker:
    """ Function for getting the ticker from Yahoo Finance API. """
    return yf.Ticker(stock_name)


def get_stock_data_from_yahoo(
        ticker: yf.Ticker, interval: str, start_date: str, end_date: str
) -> pd.DataFrame:
    """ Function for getting the historical data of a stock from Yahoo Finance API. """
    return ticker.history(
        interval=interval,
        start=start_date,
        end=end_date
    )
