import pandas as pd
from Business.Data.SignalTypes import SIGNAL_TYPES


def get_upper_bollinger_band(close_prices: pd.Series, period: int, multiplier: int) -> pd.Series:
    return close_prices.rolling(period).mean() + close_prices.rolling(period).std() * multiplier


def get_lower_bollinger_band(close_prices: pd.Series, period: int, multiplier: int) -> pd.Series:
    return close_prices.rolling(period).mean() - close_prices.rolling(period).std() * multiplier


def get_bollinger_indication(close_prices: pd.Series, upper_band: pd.Series, lower_band: pd.Series) -> SIGNAL_TYPES:
    # TODO: Bollinger indication needs conditions for trend following.
    if close_prices[-1] <= lower_band[-1]:
        return SIGNAL_TYPES.BUY
    if close_prices[-1] >= upper_band[-1]:
        return SIGNAL_TYPES.SELL
    return SIGNAL_TYPES.HOLD
