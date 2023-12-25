import pandas as pd


def getterAppendAndSetterEntryTriggeredList(row):
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
        df.loc[len(df)] = row
        df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv", index=False)
    except Exception as e:
        print(f"The exception while getter, append and setter Entry Triggered list is {e}")

