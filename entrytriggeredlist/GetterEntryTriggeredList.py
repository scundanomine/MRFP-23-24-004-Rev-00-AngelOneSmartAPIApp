import pandas as pd
from entrytriggeredlist.CleaningAndSettingETList import cleaningAndSettingETList


def getterEntryTriggeredList():
    try:
        df = pd.read_csv("F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
    except:
        # print(f"The exception while getterEntryTriggeredList is {e}")
        df = getterEntryTriggeredList()
    return df
