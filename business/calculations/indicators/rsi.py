"""
This module is for applying the RSI strategy for discovering
oversold and overbought situations of a stock.
This module also produces a buy, hold or sell signal.
"""
import pandas as pd
from business.data.signal_types import SIGNAL_TYPES


def calculate_close_price_differences(close_prices: pd.Series) -> pd.Series:
    """ Function for calculating differences between close prices. """
    return close_prices.diff()


def get_up_ewm_based_on_difference(difference: float) -> float:
    """
    Function for initializing an up ewm for the calculation of RSI.
    If the difference is negative, initialization of up ewm should be zero
    else it should be the difference.
    """
    if difference < 0:
        return 0
    return difference


def get_down_ewm_based_on_difference(difference: float) -> float:
    """
    Function for initializing an down ewm for the calculation of RSI.
    If the difference is positive, initialization of down ewm should be zero
    else it should be the difference.
    """
    if difference < 0:
        return difference
    return 0


def calculate_ewm(differences: pd.Series) -> tuple[pd.Series, pd.Series]:
    """
    Function for calculating actual ewm using the created up ewm and down ewm.
    """
    down_ewm = list(map(get_down_ewm_based_on_difference, differences))
    up_ewm = list(map(get_up_ewm_based_on_difference, differences))
    return pd.Series(up_ewm).ewm(com=13, adjust=False).mean(), \
        pd.Series(down_ewm).abs().ewm(com=13, adjust=False).mean()


def calculate_relative_strength(ewms: tuple[pd.Series, pd.Series]) -> pd.Series:
    """ Function for calculating the relative strength which is needed for RSI calculation. """
    return ewms[0] / ewms[1]


def calculate_rsi(relative_strength: pd.Series) -> pd.Series:
    """ Function for calculating RSI from the calculated relative strength. """
    return 100.0 - (100.0 / (1.0 + relative_strength))


def get_rsi_indication(rsi: pd.Series) -> SIGNAL_TYPES:
    """ Function to produce the signal based on calculated RSI signal value. """
    last_rsi = rsi.tolist()[-1]
    previous_rsi = rsi.tolist()[-2]
    if last_rsi > 70:
        return SIGNAL_TYPES.SELL
    if last_rsi < 30:
        return SIGNAL_TYPES.BUY
    if previous_rsi < last_rsi < 60:
        return SIGNAL_TYPES.BUY
    return SIGNAL_TYPES.SELL
