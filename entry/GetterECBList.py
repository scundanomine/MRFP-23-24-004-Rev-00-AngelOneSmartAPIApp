import pandas as pd
from entry.SetterPreECBList import setterPreECBList


def getterECBList(lock):
    try:
        with lock:
            df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv")
    except Exception as e:
        print(f"The exception while getterECBList is {e}")
        df = setterPreECBList(lock)
    return df


# getterECBList()
