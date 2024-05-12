import pandas as pd

from ohlcdata.GetterPreDS import getterPreDS


def getterPDS():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pastohlcdatafile\\pds.csv")
    except:
        # print(f"The exception while getterPDS is {e}")
        df = getterPDS()
    return df


# print(getterPDS())
