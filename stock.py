import requests
from environment import *
from datetime import datetime, timedelta

STOCK = "TSLA"

params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

yesterday = datetime.now() - timedelta(days=1)
while yesterday.weekday() >= 5:
    yesterday = yesterday - timedelta(days=1)

day_before = yesterday - timedelta(days=1)

response = requests.get(url=STOCK_API_END_POINT, params=params)
response.raise_for_status()

response_data = response.json()["Time Series (60min)"]

for key in response_data:
    stock_date_time = datetime.strptime(key, '%Y-%m-%d %H:%M:%S')
    if stock_date_time.hour == 20:
        if stock_date_time.year == yesterday.year and stock_date_time.month == yesterday.month and stock_date_time.day == yesterday.day:
            yesterday_close = float(response_data[key]['4. close'])
        elif stock_date_time.year == day_before.year and stock_date_time.month == day_before.month and stock_date_time.day == day_before.day:
            day_before_close = float(response_data[key]['4. close'])

do_we_get_news = ((yesterday_close - day_before_close) /
                  yesterday_close * 100)
