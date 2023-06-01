import pandas as pd
from Business.Data.SignalTypes import SIGNAL_TYPES


def calculate_close_price_differences(close_prices: pd.Series) -> pd.Series:
    return close_prices.diff()


def calculate_ewm(differences: pd.Series) -> tuple[pd.Series, pd.Series]:
    up_ewm = []
    down_ewm = []
    for difference in differences:
        if difference < 0:
            up_ewm.append(0)
            down_ewm.append(difference)
        else:
            up_ewm.append(difference)
            down_ewm.append(0)
    return pd.Series(up_ewm).ewm(com=13, adjust=False).mean(), \
        pd.Series(down_ewm).abs().ewm(com=13, adjust=False).mean()


def calculate_relative_strength(up_ewm: pd.Series, down_ewm: pd.Series) -> pd.Series:
    return up_ewm / down_ewm


def calculate_rsi(relative_strength: pd.Series) -> pd.Series:
    return 100.0 - (100.0 / (1.0 + relative_strength))


def get_rsi_indication(rsi: pd.Series) -> SIGNAL_TYPES:
    last_rsi = rsi.tolist()[-1]
    previous_rsi = rsi.tolist()[-2]
    if last_rsi > 70:
        return SIGNAL_TYPES.SELL
    if last_rsi < 30:
        return SIGNAL_TYPES.BUY
    if previous_rsi < last_rsi < 60:
        return SIGNAL_TYPES.BUY
    return SIGNAL_TYPES.SELL
