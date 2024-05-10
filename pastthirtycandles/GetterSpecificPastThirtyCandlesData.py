import pandas as pd


def getterSpecificPastThirtyCandlesData(sid, symbol):
    try:
        gdf = pd.read_csv(
                f"F:\\AT\\pastthirtycandles\\pastthirycandlesstate\\pastthirtycandlewisedata\\{sid}_{symbol}.csv")
    except Exception as e:
        print(f"The exception while getterSpecificPastThirtyCandlesData is {e}")
        gdf = getterSpecificPastThirtyCandlesData(sid, symbol)
    return gdf


# print(getterSpecificPastThirtyCandlesData(1, "RELIANCE-EQ"))
