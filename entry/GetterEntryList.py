import pandas as pd
import multiprocessing
from entry.SetterPreEntryList import setterPreEntryList


def getterEntryList(lock=multiprocessing.Lock()):
    try:
        with lock:
            df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv")
    except Exception as e:
        print(f"The exception while getterEntryList is {e}")
        df = setterPreEntryList(lock)
    return df


# getterEntryList()
