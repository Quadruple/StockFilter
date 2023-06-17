from bs4 import BeautifulSoup


def scrape_stocks_from_trading_view(page_source: str) -> list[str]:
    soup = BeautifulSoup(page_source, 'lxml')
    tables = soup.findAll("table", {"class": "table-Ngq2xrcG"})
    rows = tables[1].findAll("a", {"class": "apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat"})
    return list(map(lambda row: row.string, rows))
