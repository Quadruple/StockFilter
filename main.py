import pandas as pd
from Business.Data.SignalTypes import SIGNAL_TYPES
from Drivers.Calculations.IndexSearcher import fetch_stocks_under_bist_100_from_tradingview
from Drivers.Actions.StockFormatter import transform_bist_stock_names_into_yahoo_format
from Drivers.Calculations.StockInfoFetcher import get_stock, get_daily_stock_data
from Business.Calculations.Indicators.Macd import calculate_macd_line, calculate_signal_line, get_macd_indication, \
    is_macd_switched_to_buy_recently
from Business.Calculations.Indicators.Rsi import calculate_rsi, calculate_ewm, calculate_relative_strength, \
    calculate_close_price_differences, get_rsi_indication


def is_macd_gives_buy_signal(close_data: pd.Series) -> bool:
    if close_data.empty:
        return False
    return get_macd_indication(
        calculate_macd_line(close_data),
        calculate_signal_line(
            calculate_macd_line(close_data)
        )
    ) == SIGNAL_TYPES.BUY and is_macd_switched_to_buy_recently(
        calculate_macd_line(close_data)[-5:],
        calculate_signal_line(
            calculate_macd_line(close_data)
        )[-5:]
    )


def is_rsi_gives_buy_signal(close_data: pd.Series) -> bool:
    if close_data.empty:
        return False
    return get_rsi_indication(
        calculate_rsi(
            calculate_relative_strength(
                calculate_ewm(
                    calculate_close_price_differences(
                        close_data
                    )
                )
            )
        )
    ) == SIGNAL_TYPES.BUY


def analyze(stock_names: list[str]) -> None:
    if not stock_names:
        return
    if is_macd_gives_buy_signal(get_daily_stock_data(get_stock(stock_names[0]), year_span=1)["Close"]) and \
            is_rsi_gives_buy_signal(get_daily_stock_data(get_stock(stock_names[0]), year_span=1)["Close"]):
        print(stock_names[0])
    stock_names.pop(0)
    analyze(stock_names)


analyze(transform_bist_stock_names_into_yahoo_format(fetch_stocks_under_bist_100_from_tradingview()))
