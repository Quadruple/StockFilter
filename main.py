""" This is the driver file for initiating the analysis on stock data. """
import pandas as pd
from adapters.calculations.index_operations_adapter import scrape_component_names_under_index,\
    transform_stock_names
from adapters.calculations.emulation_adapter import get_browser_options, get_web_driver,\
    emulate_click_on_load_more_button, open_url_in_driver, get_url_to_scrape_components
from adapters.calculations.stock_info_adapter import get_stock, get_stock_data
from business.data.signal_types import SIGNAL_TYPES
from business.calculations.indicators.macd import calculate_macd_line, \
    calculate_signal_line, get_macd_indication, is_macd_switched_to_buy_recently
from business.calculations.indicators.rsi import calculate_rsi, \
    calculate_ewm, calculate_relative_strength, \
    calculate_close_price_differences, get_rsi_indication
from business.calculations.indicators.bollinger_bands import get_lower_bollinger_band, \
    get_upper_bollinger_band, get_bollinger_indication
from business.calculations.dates import get_years_ago, get_today, \
    transform_date_to_year_month_date_format


def is_macd_gives_buy_signal(close_data: pd.Series) -> bool:
    """ Function for checking the macd analysis if it gives buy signal. """
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
    """ Function for checking the rsi analysis if it gives buy signal. """
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
    """ Function for checking the bollinger band analysis if it gives buy signal. """
    return get_bollinger_indication(
        close_data,
        get_upper_bollinger_band(close_data, 20, 2),
        get_lower_bollinger_band(close_data, 20, 2)
    )


def analyze(stock_names: list[str]) -> None:
    """
    Function for checking all the technical analysis results if they all give buy signals.
    If all the technical indicators give buy signal, it reports the stock name for a buy potential.
    """
    if not stock_names:
        return
    if is_macd_gives_buy_signal(
        get_stock_data(
            get_stock(stock_names[0]),
            "1d",
            transform_date_to_year_month_date_format(get_years_ago(1)),
            transform_date_to_year_month_date_format(get_today())
        )["Close"]
    ) and is_rsi_gives_buy_signal(
        get_stock_data(
            get_stock(stock_names[0]),
            "1d",
            transform_date_to_year_month_date_format(get_years_ago(1)),
            transform_date_to_year_month_date_format(get_today())
        )["Close"]
    ) and is_bollinger_gives_buy_signal(
        get_stock_data(
            get_stock(stock_names[0]),
            "1d",
            transform_date_to_year_month_date_format(get_years_ago(1)),
            transform_date_to_year_month_date_format(get_today())
        )["Close"]
    ):
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
