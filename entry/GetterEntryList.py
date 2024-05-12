import pandas as pd


def getterEntryList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv")
    except:
        # print(f"The exception while getterEntryList is {e}")
        df = getterEntryList()
    return df


# getterEntryList()
