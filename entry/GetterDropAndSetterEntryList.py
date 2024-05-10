import pandas as pd


def getterDropAndSetterEntryList(uid):
    try:
        df = pd.read_csv("F:\\AT\\entry\\entrystate\\EntryList.csv")
        i = df[(df.id == uid)].index
        df = df.drop(i)
        df.to_csv("F:\\AT\\entry\\entrystate\\EntryList.csv", index=False)
    except Exception as e:
        print(f"The exception while getterDropAndSetterEntryList is {e}")
        getterDropAndSetterEntryList(uid)

