import pandas as pd


def getterPreSpecificHistoricData(date, sid):
    try:
        gdf = pd.read_csv(
                f"F:\\AT\\historicdata\\historicdatastate\\{date}\\{sid}.csv")
    except Exception as e:
        print(f"The exception while getterPreSpecificHistoricData is {e}")
        gdf = getterPreSpecificHistoricData(date, sid)
    return gdf


# print(getterSpecificHistoricData("2024-04-16", 10))
