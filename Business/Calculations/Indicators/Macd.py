import pandas as pd
from Business.Data.SignalTypes import SIGNAL_TYPES


def calculate_macd_line(close_prices: pd.Series) -> pd.Series:
    ema_12 = close_prices.ewm(span=12, adjust=False).mean()
    ema_26 = close_prices.ewm(span=26, adjust=False).mean()
    return ema_12 - ema_26


def calculate_signal_line(macd_line: pd.Series) -> pd.Series:
    return macd_line.ewm(span=9, adjust=False).mean()


def get_macd_indication(macd_line: pd.Series, signal_line: pd.Series) -> SIGNAL_TYPES:
    if macd_line[-1] > signal_line[-1]:
        return SIGNAL_TYPES.BUY
    else:
        return SIGNAL_TYPES.SELL


def is_macd_switched_to_buy_recently(last_macd: pd.Series, last_signal: pd.Series) -> bool:
    if last_macd.empty or last_signal.empty:
        return False
    if last_macd[0] < last_signal[0]:
        return True
    last_macd = last_macd.drop(last_macd.index[0])
    last_signal = last_signal.drop(last_signal.index[0])
    return is_macd_switched_to_buy_recently(last_macd, last_signal)
