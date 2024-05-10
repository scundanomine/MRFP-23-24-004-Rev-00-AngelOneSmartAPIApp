import pandas as pd


def getCandlestickDf():
    kdf = pd.read_csv(
        "F:\\AT\\candlestickdata\\candle_state\\gstData.csv")
    return kdf


getCandlestickDf()
