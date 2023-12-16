import pandas as pd
import multiprocessing

from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList


def setterPreECBList(lock=multiprocessing.Lock()):
    lock.acquire()
    df = getterRequiredSymbolAndTokenList()
    lock.release()
    df = df.loc[:, ['id']]
    # flag for entry calculation
    df['eCBFlag'] = False
    lock.acquire()
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv",
        index=False)
    lock.release()
    return df


# print(setterPreECBList())
