import pandas as pd


def getterEntryList():
    try:
        df = pd.read_csv("F:\\AT\\entry\\entrystate\\EntryList.csv")
    except:
        # print(f"The exception while getterEntryList is {e}")
        df = getterEntryList()
    return df


# getterEntryList()
