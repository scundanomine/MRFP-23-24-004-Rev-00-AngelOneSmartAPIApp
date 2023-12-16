import pandas as pd
from ohlcdata.GetterPreDS import getterPreDS


def getterFFDS():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\ffds.csv")
    except Exception as e:
        print(f"The exception while getter future future ds is {e}")
        df = getterPreDS()
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\ffds.csv",
            index=False)
    return df


# print(getterFDS())
