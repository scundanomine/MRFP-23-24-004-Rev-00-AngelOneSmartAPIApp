import pandas as pd


def getterPDS():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pastohlcdatafile\\pds.csv")
    except Exception as e:
        print(f"The exception while getter Past Ds is {e}")
        df = pd.DataFrame(columns=[0, 1, 2, 3, 4, 5], index=list(range(500)))
        df[:] = 0
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pastohlcdatafile\\pds.csv",
            index=False)
    return df


# print(getterPDS())
