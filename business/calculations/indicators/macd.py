"""
This module is for applying the moving average convergence divergence to the stock data.
Based on the calculated MACD and signal lines a buy, sell or hold signal is produced.
"""
import pandas as pd
from business.data.signal_types import SIGNAL_TYPES


def calculate_macd_line(close_prices: pd.Series) -> pd.Series:
    """ Function for calculating the macd line from close prices. """
    ema_12 = close_prices.ewm(span=12, adjust=False).mean()
    ema_26 = close_prices.ewm(span=26, adjust=False).mean()
    return ema_12 - ema_26


def calculate_signal_line(macd_line: pd.Series) -> pd.Series:
    """ Function for calculating the signal line from close prices. """
    return macd_line.ewm(span=9, adjust=False).mean()


def get_macd_indication(macd_line: pd.Series, signal_line: pd.Series) -> SIGNAL_TYPES:
    """ Function for getting the macd indication signal. """
    if macd_line[-1] > signal_line[-1]:
        return SIGNAL_TYPES.BUY
    return SIGNAL_TYPES.SELL


def is_macd_switched_to_buy_recently(last_macd: pd.Series, last_signal: pd.Series) -> bool:
    """
    Function for discovering if a stock is switched to buy recently
    by giving the last values of macd and signal lines.
     """
    if last_macd.empty or last_signal.empty:
        return False
    if last_macd[0] < last_signal[0]:
        return True
    last_macd = last_macd.drop(last_macd.index[0])
    last_signal = last_signal.drop(last_signal.index[0])
    return is_macd_switched_to_buy_recently(last_macd, last_signal)
