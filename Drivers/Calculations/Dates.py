from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_today() -> datetime:
    return datetime.today()


def get_years_ago(years: int) -> datetime:
    return datetime.today() - relativedelta(years=years)


def transform_date_to_year_month_date_format(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")
