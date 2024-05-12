import pandas as pd


def getterEntryBannedDf():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\positionportfolioandmargindisplay\\displaystate\\EntryBanned.csv")
    except Exception as e:
        print(f"The exception while getter getterEntryBannedDf is {e}")
        df = getterEntryBannedDf()
    return df


# print(getterEntryBannedDf())
