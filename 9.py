from tardis_dev import datasets

def download(start_time, end_date):
    datasets.download(
    exchange="bybit",
    data_types=[
      "quotes",
      "liquidations",
      "derivative_ticker",
      "trades"
    ],
    from_date=start_time,
    to_date=end_date,
    symbols=["BTCUSD"],
    api_key="TD.9wkdm9sOpHKRn5zV.YN9Bl-Hd8Q9DfO7.g0zG3MmyiXpVEb9.U9iW0oOPu0HTaSa.gbTdYT7GV8tTc7B.NSzm")

#Example Download
download("2022-01-02", "2022-04-01") 

