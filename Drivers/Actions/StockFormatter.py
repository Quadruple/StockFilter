from Drivers.Data.ComponentData import yahoo_country_code


def transform_stock_names_into_yahoo_format(stocks: list[str]) -> list[str]:
    return list(map(lambda x: x + yahoo_country_code, stocks))
