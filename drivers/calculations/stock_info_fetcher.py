"""
This module is an extension to stock info adapter.
Its responsibility is to provide functionalities on Yahoo Finance API
such as fetching a stocks data.
"""
import yfinance as yf
import pandas as pd
from drivers.calculations.dates import get_today, get_years_ago, \
    transform_date_to_year_month_date_format


def get_stock_from_yahoo(stock_name: str) -> yf.Ticker:
    """ Function for getting the ticker from Yahoo Finance API. """
    return yf.Ticker(stock_name)


def get_daily_stock_data_from_yahoo(ticker: yf.Ticker, year_span: int) -> pd.DataFrame:
    """ Function for getting the daily historical data from year_span years ago till today. """
    return ticker.history(
        period="1d",
        start=transform_date_to_year_month_date_format(get_years_ago(year_span)),
        end=transform_date_to_year_month_date_format(get_today())
    )
