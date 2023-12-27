import xlwings as xw
import pandas as pd
from commonudm.GetterStockQtn import getterStockQtn
import multiprocessing


def getCustomDfExitInputs(lock=multiprocessing.Lock()):
    # startTime = time.time()
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets("ExitInput")
    lock.acquire()
    n = getterStockQtn()

    df = pd.DataFrame(dt.range(f"a{2}:c{n+1}").value, columns=["id", 'rFlag', 'eFlag'])
    lock.release()
    df = df.astype("int64")
    return df


# print(getCustomDfExitInputs())
