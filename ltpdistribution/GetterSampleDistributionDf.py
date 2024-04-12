import pandas as pd


def getterSampleDistributionDf():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\SDDf.csv")
    except:
        # print(f"The exception while getterEntryTriggeredList is {e}")
        df = getterSampleDistributionDf()
    return df
