import pandas as pd


def getterDropAndSetterEntryList(uid):
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv")
        i = df[(df.id == uid)].index
        df = df.drop(i)
        df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv", index=False)
    except Exception as e:
        print(f"The exception while getter, Drop and setter Entry List is {e}")

