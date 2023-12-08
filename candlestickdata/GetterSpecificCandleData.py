import pandas as pd


def getterSpecificCandleData(sid, symbol):
    try:
        gdf = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv")
    except Exception as e:
        print(f"The exception while getter specific candle data is {e}")
        gdf = pd.DataFrame(columns=list(range(6)), index=list(range(10)))
        gdf[:] = 0
    return gdf


# print(getterPDS())
