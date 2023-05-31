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


def is_macd_switched_to_buy_recently(macd_line: pd.Series, signal_line: pd.Series) -> bool:
    last_5_days_macd = macd_line[-5:]
    last_5_days_signal = signal_line[-5:]
    for index in range(len(last_5_days_signal)):
        if last_5_days_macd[index] < last_5_days_signal[index]:
            return True
    return False
