import pandas as pd
from entrytriggeredlist.CleaningAndSettingETList import cleaningAndSettingETList


def getterEntryTriggeredList(lock):
    try:
        lock.acquire()
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
        lock.release()
    except Exception as e:
        print(f"The exception while getter Order list is {e}")
        cleaningAndSettingETList(lock)
        lock.acquire()
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
        lock.release()
    return df
