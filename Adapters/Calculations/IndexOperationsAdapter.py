from Drivers.Calculations.IndexSearcher import scrape_stocks_from_trading_view
from Drivers.Actions.StockFormatter import transform_stock_names_into_yahoo_format


def scrape_component_names_under_index(page_source: str) -> list[str]:
    return scrape_stocks_from_trading_view(page_source)


def transform_stock_names(stocks: list[str]) -> list[str]:
    return transform_stock_names_into_yahoo_format(stocks)
