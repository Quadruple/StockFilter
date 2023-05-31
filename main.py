from Drivers.Calculations.IndexSearcher import fetch_stocks_under_bist_100_from_tradingview
from Drivers.Actions.StockFormatter import transform_bist_stock_names_into_yahoo_format
from Drivers.Calculations.StockInfoFetcher import get_stock, get_daily_stock_data
from Business.Calculations.Indicators.Macd import calculate_macd_line, calculate_signal_line, get_indication, \
    is_macd_switched_to_buy_recently
from Business.Data.SignalTypes import SIGNAL_TYPES


bist_100_stock_names = transform_bist_stock_names_into_yahoo_format(fetch_stocks_under_bist_100_from_tradingview())
for stock_name in bist_100_stock_names:
    data = get_daily_stock_data(get_stock(stock_name))
    macd = calculate_macd_line(data["Close"])
    signal = calculate_signal_line(macd)
    if get_indication(macd, signal) == SIGNAL_TYPES.BUY and is_macd_switched_to_buy_recently(macd, signal):
        print(stock_name)
