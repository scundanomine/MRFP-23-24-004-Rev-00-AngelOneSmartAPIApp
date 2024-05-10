import pandas as pd


def getCandlestickTenMinuteData():
    cdf = pd.read_csv(
        "F:\\AT\\candlestickdata\\candle_state\\gstData.csv")
    return cdf


def saveCandlestickTenMinuteData(cdf):
    cdf.to_csv(
        "F:\\AT\\candlestickdata\\candle_state\\gstData.csv",
        index=False)
