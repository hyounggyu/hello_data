import os
import time
import urllib.parse

from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

TOKEN = os.getenv("ALPHAVANTAGE_API_KEY")


def fetch(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": TOKEN,
        "datatype": "csv",
    }
    query = urllib.parse.urlencode(params)
    r = requests.get(
        f"https://www.alphavantage.co/query?{query}",
    )
    with open(f"../data/alphavantage/{symbol}.csv", "w") as f:
        f.write(r.text)


def main():
    df = pd.read_csv("../data/datahub/s-and-p-500-companies.csv")
    for symbol in sorted(df.Symbol.to_list()):
        print(f"Fetching... {symbol}")
        fetch(symbol)
        time.sleep(1)


if __name__ == "__main__":
    main()
