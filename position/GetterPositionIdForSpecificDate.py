import pandas as pd


def getterPositionIdForSpecificDate(rDate):
    try:
        df = pd.read_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{rDate}\\state\\PId.csv")
    except:
        # print(f"The exception while getter Position list is {e}")
        df = getterPositionIdForSpecificDate(rDate)
    return df.loc[0, "pid"]


# getterEntryList()
