"""
This module also is an extension to the index operations adapter.
It is only responsible from scraping all stock names under an index from TradingView
using BeautifulSoup module.
"""
from bs4 import BeautifulSoup


def scrape_stocks_from_trading_view(page_source: str) -> list[str]:
    """ Function for scraping all stock names from the tables presented in TradingView. """
    return list(
        map(
            lambda row: row.string, BeautifulSoup(page_source, 'lxml')
            .findAll("table", {"class": "table-Ngq2xrcG"})[1]
            .findAll(
                "a",
                {"class": "apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat"}
            )
        )
    )
