import pandas as pd


def getterPositionList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
    except:
        # print(f"The exception while getter Position list is {e}")
        df = getterPositionList()
    return df


# getterEntryList()
