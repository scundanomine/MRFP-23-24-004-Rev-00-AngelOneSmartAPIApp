import pandas as pd


def getterPastTenCandleDf(sid):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{sid}.csv")
    except Exception as e:
        print(f"The exception while getter Past 10 candle df is {e}")
        df = pd.DataFrame(columns=[0, 1, 2, 3, 4, 5], index=list(range(10)))
        df[:] = 0
        df.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{sid}.csv",
            index=False)
    return df


# print(getterFDS())
