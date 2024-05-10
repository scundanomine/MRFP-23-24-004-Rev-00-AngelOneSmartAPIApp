import pandas as pd


def getterSpecificCandleData(sid, symbol):
    try:
        gdf = pd.read_csv(
                f"F:\\AT\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv")
    except:
        # print(f"The exception while getterSpecificCandleData is {e}")
        gdf = getterSpecificCandleData(sid, symbol)
    return gdf


# print(getterPDS())
