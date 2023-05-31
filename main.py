from Business.Data.SignalTypes import SIGNAL_TYPES
from Drivers.Calculations.IndexSearcher import fetch_stocks_under_bist_100_from_tradingview
from Drivers.Actions.StockFormatter import transform_bist_stock_names_into_yahoo_format
from Drivers.Calculations.StockInfoFetcher import get_stock, get_daily_stock_data
from Business.Calculations.Indicators.Macd import calculate_macd_line, calculate_signal_line, get_macd_indication, \
    is_macd_switched_to_buy_recently
from Business.Calculations.Indicators.Rsi import calculate_rsi, calculate_ewm, calculate_relative_strength, \
    calculate_close_price_differences, get_rsi_indication


bist_100_stock_names = transform_bist_stock_names_into_yahoo_format(fetch_stocks_under_bist_100_from_tradingview())
for stock_name in bist_100_stock_names:
    data = get_daily_stock_data(get_stock(stock_name), year_span=1)
    macd = calculate_macd_line(data["Close"])
    signal = calculate_signal_line(macd)
    differences = calculate_close_price_differences(data["Close"])
    up_ewm, down_ewm = calculate_ewm(differences)
    relative_strength = calculate_relative_strength(up_ewm, down_ewm)
    rsi = calculate_rsi(relative_strength)
    if get_macd_indication(macd, signal) == SIGNAL_TYPES.BUY and is_macd_switched_to_buy_recently(macd, signal) and \
            get_rsi_indication(rsi) == SIGNAL_TYPES.BUY:
        print(stock_name)
