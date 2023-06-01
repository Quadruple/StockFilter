import yfinance as yf
import pandas as pd
from Drivers.Calculations.Dates import get_today, get_years_ago, transform_date_to_year_month_date_format


def get_stock(stock_name: str) -> yf.Ticker:
    return yf.Ticker(stock_name)


def get_daily_stock_data(ticker: yf.Ticker, year_span: int) -> pd.DataFrame:
    return ticker.history(
        period="1d",
        start=transform_date_to_year_month_date_format(get_years_ago(year_span)),
        end=transform_date_to_year_month_date_format(get_today())
    )
