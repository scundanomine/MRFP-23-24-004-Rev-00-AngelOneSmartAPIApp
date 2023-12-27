import pandas as pd
import multiprocessing
from position.SetterPrePositionList import setterPrePositionList


def getterPositionList(lock=multiprocessing.Lock()):
    try:
        lock.acquire()
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
        lock.release()
    except Exception as e:
        print(f"The exception while getter Position list is {e}")
        df = setterPrePositionList(lock)
    return df


# getterEntryList()
