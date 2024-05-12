import pandas as pd


def getterSpecificPastThirtyCandlesData(sid, symbol):
    try:
        gdf = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\pastthirtycandlewisedata\\{sid}_{symbol}.csv")
    except Exception as e:
        print(f"The exception while getterSpecificPastThirtyCandlesData is {e}")
        gdf = getterSpecificPastThirtyCandlesData(sid, symbol)
    return gdf


# print(getterSpecificPastThirtyCandlesData(1, "RELIANCE-EQ"))
