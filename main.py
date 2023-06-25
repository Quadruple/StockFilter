import pandas as pd
from adapters.calculations.IndexOperationsAdapter import scrape_component_names_under_index, transform_stock_names
from adapters.calculations.EmulationAdapter import get_browser_options, get_web_driver,\
    emulate_click_on_load_more_button, open_url_in_driver, get_url_to_scrape_components
from adapters.calculations.StockInfoAdapter import get_stock, get_daily_stock_data
from business.data.SignalTypes import SIGNAL_TYPES
from business.calculations.indicators.Macd import calculate_macd_line, calculate_signal_line, get_macd_indication, \
    is_macd_switched_to_buy_recently
from business.calculations.indicators.Rsi import calculate_rsi, calculate_ewm, calculate_relative_strength, \
    calculate_close_price_differences, get_rsi_indication
from business.calculations.indicators.BollingerBands import get_lower_bollinger_band, get_upper_bollinger_band, \
    get_bollinger_indication


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


def is_bollinger_gives_buy_signal(close_data: pd.Series) -> bool:
    return get_bollinger_indication(
        close_data,
        get_upper_bollinger_band(close_data, 20, 2),
        get_lower_bollinger_band(close_data, 20, 2)
    )


def analyze(stock_names: list[str]) -> None:
    if not stock_names:
        return
    if is_macd_gives_buy_signal(get_daily_stock_data(get_stock(stock_names[0]), year_span=1)["Close"]) and \
            is_rsi_gives_buy_signal(get_daily_stock_data(get_stock(stock_names[0]), year_span=1)["Close"]) and \
            is_bollinger_gives_buy_signal(get_daily_stock_data(get_stock(stock_names[0]), year_span=1)["Close"]):
        print(stock_names[0])
    stock_names.pop(0)
    analyze(stock_names)


analyze(
    transform_stock_names(
        scrape_component_names_under_index(
            emulate_click_on_load_more_button(
                open_url_in_driver(
                    get_url_to_scrape_components(),
                    get_web_driver(
                        get_browser_options()
                    )
                )
            )
        )
    )
)
