import pandas as pd


def getterEntryList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv")
    except Exception as e:
        print(f"The exception while getter Entry list is {e}")
        df = pd.DataFrame(columns=["id", "ltp", "lp", "q", "sl", "target"])
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv",
            index=False)
    return df


# getterEntryList()
