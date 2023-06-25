"""
This module is for applying the bollinger band strategy and obtain buy, sell or hold signal.
"""
import pandas as pd
from business.data.signal_types import SIGNAL_TYPES


def get_upper_bollinger_band(close_prices: pd.Series, period: int, multiplier: int) -> pd.Series:
    """ Function for calculating upper bollinger band from close prices. """
    return close_prices.rolling(period).mean() + close_prices.rolling(period).std() * multiplier


def get_lower_bollinger_band(close_prices: pd.Series, period: int, multiplier: int) -> pd.Series:
    """ Function for calculating lower bollinger band from close prices. """
    return close_prices.rolling(period).mean() - close_prices.rolling(period).std() * multiplier


def get_bollinger_indication(
        close_prices: pd.Series, upper_band: pd.Series, lower_band: pd.Series) -> SIGNAL_TYPES:
    """ Function for discovering a signal through calculated upper and lower bollinger bands. """
    if close_prices[-1] <= lower_band[-1]:
        return SIGNAL_TYPES.BUY
    if close_prices[-1] >= upper_band[-1]:
        return SIGNAL_TYPES.SELL
    return SIGNAL_TYPES.HOLD
