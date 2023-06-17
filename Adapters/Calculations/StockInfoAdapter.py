import pandas as pd
import yfinance as yf
from Drivers.Calculations.StockInfoFetcher import get_stock_from_yahoo, get_daily_stock_data_from_yahoo


def get_stock(stock_name: str) -> yf.Ticker:
    return get_stock_from_yahoo(stock_name)


def get_daily_stock_data(ticker: yf.Ticker, year_span: int) -> pd.DataFrame:
    return get_daily_stock_data_from_yahoo(ticker, year_span)
