import pandas as pd


def getterFFDS():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\ffds.csv")
    except Exception as e:
        # print(f"The exception while getter future future ds is {e}")
        a = e
        df = getterFFDS()
    return df


# print(getterFDS())
