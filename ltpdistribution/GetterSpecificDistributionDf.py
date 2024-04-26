import pandas as pd


def getterSpecificDistributionDf(uid):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv")
    except Exception as e:
        print(f"The exception while getterSpecificDistributionDf is {e}")
        df = getterSpecificDistributionDf(uid)
    return df


# print(getterSpecificDistributionDf("specificdistributiondf", 1))
