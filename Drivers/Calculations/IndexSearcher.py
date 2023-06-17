import requests
from bs4 import BeautifulSoup


def fetch_stocks_under_bist_100_from_tradingview() -> list[str]:
    url = "https://tr.tradingview.com/symbols/BIST-XU100/components/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find("table")
    rows = table.findAll("a", {"class": "apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat"})
    return list(map(lambda row: row.string, rows))


def fetch_stocks_from_trading_view(page_source: str) -> list[str]:
    soup = BeautifulSoup(page_source, 'lxml')
    tables = soup.findAll("table", {"class": "table-Ngq2xrcG"})
    rows = tables[1].findAll("a", {"class": "apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat"})
    return list(map(lambda row: row.string, rows))
