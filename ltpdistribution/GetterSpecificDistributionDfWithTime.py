import pandas as pd


def getterPartlySpecificDistributionDf(uid):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv")
        df.set_index("time", inplace=True)
    except Exception as e:
        print(f"The exception while getterPartlySpecificDistributionDf is {e}")
        df = getterPartlySpecificDistributionDf(uid)
    return df


# print(getterPartlySpecificDistributionDf("specificdistributiondf", 1))
