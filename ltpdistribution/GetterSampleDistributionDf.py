import pandas as pd


def getterSampleDistributionDf():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\SDDf.csv")
        df = df.set_index('time')
    except Exception as e:
        print(f"The exception while getterSampleDistributionDf is {e}")
        df = getterSampleDistributionDf()
    return df


# print(getterSampleDistributionDf())
