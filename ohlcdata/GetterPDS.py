import pandas as pd

from ohlcdata.GetterPreDS import getterPreDS


def getterPDS():
    try:
        df = pd.read_csv(
            "F:\\AT\\ohlcdata\\ohlcstate\\pastohlcdatafile\\pds.csv")
    except:
        # print(f"The exception while getterPDS is {e}")
        df = getterPDS()
    return df


# print(getterPDS())
