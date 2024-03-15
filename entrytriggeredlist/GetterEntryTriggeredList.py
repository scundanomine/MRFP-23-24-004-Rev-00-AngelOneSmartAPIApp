import pandas as pd
from entrytriggeredlist.CleaningAndSettingETList import cleaningAndSettingETList


def getterEntryTriggeredList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
    except:
        # print(f"The exception while getterEntryTriggeredList is {e}")
        df = getterEntryTriggeredList()
    return df
