def transform_bist_stock_names_into_yahoo_format(stocks: list[str]) -> list:
    return [stock + ".IS" for stock in stocks]
