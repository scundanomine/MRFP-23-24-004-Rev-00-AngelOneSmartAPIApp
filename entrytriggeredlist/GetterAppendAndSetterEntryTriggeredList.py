import pandas as pd


def getterAppendAndSetterEntryTriggeredList(row):
    try:
        df = pd.read_csv("F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
        df.loc[len(df)] = row
        df.to_csv("F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv", index=False)
    except Exception as e:
        print(f"The exception while getter, append and setter Entry Triggered list is {e}")
        getterAppendAndSetterEntryTriggeredList(row)

