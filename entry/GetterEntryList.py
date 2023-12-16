import pandas as pd

from entry.SetterPreEntryList import setterPreEntryList


def getterEntryList(lock):
    try:
        lock.acquire()
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv")
        lock.release()
    except Exception as e:
        print(f"The exception while getter Entry list is {e}")
        df = setterPreEntryList(lock)
    return df


getterEntryList()
