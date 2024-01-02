import xlwings as xw
import pandas as pd
from commonudm.GetterStockQtn import getterStockQtn
import time
import multiprocessing


def getCustomDfBlackListET(lock=multiprocessing.Lock()):
    # startTime = time.time()
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("BlackList")
            lock.acquire()
            n = getterStockQtn()
            lock.release()
            df = pd.DataFrame(dt.range(f"a{2}:b{n+1}").value, columns=["id", 'bFlag'])
            break
        except Exception as e:
            print(f"Exception while getCustomDfBlackListET is {e}")
    df["id"] = df["id"].astype("int64")
    df["bFlag"] = df["bFlag"].astype("int64")
    # print(f"execution time for getting CustomDfBlackListET {time.time()-startTime}")
    return df


# print(getCustomDfBlackListET())
