import requests
from bs4 import BeautifulSoup


def fetch_stocks_under_bist_100_from_tradingview() -> list[str]:
    url = "https://tr.tradingview.com/symbols/BIST-XU100/components/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find("table")
    rows = table.findAll("a", {"class": "apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat"})
    return list(map(lambda row: row.string, rows))
