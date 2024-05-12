import pandas as pd


def getterFDS():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\fds.csv")
    except Exception as e:
        # print(f"The exception while getterFDS is {e}")
        a = e
        df = getterFDS()
    return df


# print(getterFDS())
