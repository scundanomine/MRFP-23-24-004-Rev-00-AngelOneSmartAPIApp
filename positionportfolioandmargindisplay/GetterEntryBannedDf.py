import pandas as pd


def getterEntryBannedDf():
    try:
        df = pd.read_csv(
            "F:\\AT\\positionportfolioandmargindisplay\\displaystate\\EntryBanned.csv")
    except Exception as e:
        print(f"The exception while getter getterEntryBannedDf is {e}")
        df = getterEntryBannedDf()
    return df


# print(getterEntryBannedDf())
