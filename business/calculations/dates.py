"""
This module provides the datetime functionalities required
while fetching data or analysing stocks.
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_today() -> datetime:
    """ Function for obtaining today's date from datetime. """
    return datetime.today()


def get_years_ago(years: int) -> datetime:
    """ Function for obtaining the date of given years ago. """
    return datetime.today() - relativedelta(years=years)


def get_days_ago(days: int) -> datetime:
    """ Function for obtaining the date of given days ago. """
    return datetime.today() - relativedelta(days=days)


def transform_date_to_year_month_date_format(date: datetime) -> str:
    """ Function for formatting the given date into year-month-day format string. """
    return date.strftime("%Y-%m-%d")
