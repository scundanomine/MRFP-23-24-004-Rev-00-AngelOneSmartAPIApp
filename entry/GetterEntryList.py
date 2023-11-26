import pandas as pd


def getterEntryList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv")
    except Exception as e:
        print(f"The exception while getter Entry list is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        # mr is margin required, lp is limit price, q is the quantity, sl is the stop loss
        df = pd.DataFrame(columns=["id", "ltp", "lp", "q", "sl", "target", "mr", "po", "sl", "to", "top"])
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv",
            index=False)
    return df


getterEntryList()
