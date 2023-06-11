import pandas as pd


def get_upper_bollinger_band(close_prices: pd.Series, period: int, multiplier: int) -> pd.Series:
    return close_prices.rolling(period).mean() + close_prices.rolling(period).std() * multiplier


def get_lower_bollinger_band(close_prices: pd.Series, period: int, multiplier: int) -> pd.Series:
    return close_prices.rolling(period).mean() - close_prices.rolling(period).std() * multiplier
