"""
This module is an extension to the index operations adapter.
It's responsibility is to provide compatibility between TradingView
and Yahoo Finance API.
An example can be given from BIST100 index;
In TradingView the stock AKSEN is displayed as AKSEN.IS in Yahoo Finance API.
For compatibility, a transformation module is required.
"""
from drivers.data.component_data import yahoo_country_code


def transform_stock_names_into_yahoo_format(stocks: list[str]) -> list[str]:
    """
    Function for adding the required country code to the stock name so that
    its data can be retrieved from Yahoo Finance API.
    """
    return list(map(lambda x: x + yahoo_country_code, stocks))
