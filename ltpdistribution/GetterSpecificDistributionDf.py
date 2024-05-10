import pandas as pd


def getterSpecificDistributionDf(uid):
    try:
        df = pd.read_csv(
            f"F:\\AT\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv")
    except Exception as e:
        print(f"The exception while getterSpecificDistributionDf is {e}")
        df = getterSpecificDistributionDf(uid)
    return df


# print(getterSpecificDistributionDf("specificdistributiondf", 1))
