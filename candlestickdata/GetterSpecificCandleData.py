import pandas as pd


def getterSpecificCandleData(sid, symbol):
    try:
        gdf = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv")
    except:
        # print(f"The exception while getterSpecificCandleData is {e}")
        gdf = getterSpecificCandleData(sid, symbol)
    return gdf


# print(getterSpecificCandleData(120, "Nifty 50"))
