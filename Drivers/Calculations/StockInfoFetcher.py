import yfinance as yf
import pandas as pd


def get_stock(stock_name: str) -> yf.Ticker:
    return yf.Ticker(stock_name)


def get_daily_stock_data(ticker: yf.Ticker) -> pd.DataFrame:
    return ticker.history()
