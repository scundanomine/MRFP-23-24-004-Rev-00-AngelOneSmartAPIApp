import pandas as pd


def getterSpecificLtpDistributionWithTimeIndex(date, sid):
    try:
        gdf = pd.read_csv(
                f"F:\\AT\\ltpdistribution\\ltpdistributionstate\\allcandledistributiondf\\{date}\\{sid}.csv")
        gdf = gdf.set_index('time')
    except Exception as e:
        print(f"The exception while getterSpecificLtpDistributionWithTimeIndex is {e}")
        gdf = getterSpecificLtpDistributionWithTimeIndex(date, sid)
    return gdf


# print(getterSpecificHistoricData("2024-04-16", 10))
