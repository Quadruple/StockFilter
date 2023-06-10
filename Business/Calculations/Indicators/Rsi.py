import pandas as pd
from Business.Data.SignalTypes import SIGNAL_TYPES


def calculate_close_price_differences(close_prices: pd.Series) -> pd.Series:
    return close_prices.diff()


def get_up_ewm_based_on_difference(difference: float) -> float:
    if difference < 0:
        return 0
    return difference


def get_down_ewm_based_on_difference(difference: float) -> float:
    if difference < 0:
        return difference
    return 0


def calculate_ewm(differences: pd.Series) -> tuple[pd.Series, pd.Series]:
    down_ewm = list(map(get_down_ewm_based_on_difference, differences))
    up_ewm = list(map(get_up_ewm_based_on_difference, differences))
    return pd.Series(up_ewm).ewm(com=13, adjust=False).mean(), \
        pd.Series(down_ewm).abs().ewm(com=13, adjust=False).mean()


def calculate_relative_strength(ewms: tuple[pd.Series, pd.Series]) -> pd.Series:
    return ewms[0] / ewms[1]


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
