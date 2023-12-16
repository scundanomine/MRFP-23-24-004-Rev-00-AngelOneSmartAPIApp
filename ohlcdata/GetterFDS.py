import pandas as pd
from ohlcdata.GetterPreDS import getterPreDS


def getterFDS():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\fds.csv")
    except Exception as e:
        print(f"The exception while getter Past Ds is {e}")
        df = getterPreDS()
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\fds.csv",
            index=False)
    return df


# print(getterFDS())
