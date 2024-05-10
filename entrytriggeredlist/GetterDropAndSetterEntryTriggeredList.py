import pandas as pd


def getterDropAndSetterEntryTriggeredList(uid):
    try:
        df = pd.read_csv("F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
        i = df[(df.id == uid)].index
        df = df.drop(i)
        df.to_csv("F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv", index=False)
    except Exception as e:
        print(f"The exception while getterDropAndSetterEntryTriggeredList is {e}")
        getterDropAndSetterEntryTriggeredList(uid)

