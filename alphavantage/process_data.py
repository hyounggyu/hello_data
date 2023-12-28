import pathlib

import pandas as pd


def process_data(path):
    for p in pathlib.Path(path).glob("*.csv"):
        symbol = p.stem.split(".")[0]
        df = pd.read_csv(p)
        df["symbol"] = symbol
        df["close"] = df["close"] / df["close"].iloc[-1]
        df.sort_values(by=['timestamp'], inplace=True)
        df.to_csv(p, columns=["timestamp", "symbol", "close"], index=False)


if __name__ == "__main__":
    process_data("../data/alphavantage")
