import pandas as pd


def getterAppendAndSetterEntryList(row):
    try:
        df = pd.read_csv("F:\\AT\\entry\\entrystate\\EntryList.csv")
        df.loc[len(df)] = row
        df.to_csv("F:\\AT\\entry\\entrystate\\EntryList.csv", index=False)
    except Exception as e:
        print(f"The exception while getter, append and setter Entry List is {e}")
        getterAppendAndSetterEntryList(row)

