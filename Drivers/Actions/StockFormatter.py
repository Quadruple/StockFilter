def transform_bist_stock_names_into_yahoo_format(stocks: list[str]) -> list:
    return list(map(lambda x: x + ".IS", stocks))
