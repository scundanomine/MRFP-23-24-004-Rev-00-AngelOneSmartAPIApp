import pandas as pd


def getterSpecificHistoricData(date, sid):
    try:
        gdf = pd.read_csv(
                f"F:\\AT\\historicdata\\historicdatastate\\{date}\\{sid}.csv")
        gdf = gdf.set_index('time')
    except Exception as e:
        print(f"The exception while getterSpecificCandleData is {e}")
        gdf = getterSpecificHistoricData(date, sid)
    return gdf


# print(getterSpecificHistoricData("2024-04-16", 10))
