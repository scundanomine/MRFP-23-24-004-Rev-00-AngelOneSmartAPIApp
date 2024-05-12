import pandas as pd


def getCandlestickDf():
    kdf = pd.read_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv")
    return kdf


getCandlestickDf()
