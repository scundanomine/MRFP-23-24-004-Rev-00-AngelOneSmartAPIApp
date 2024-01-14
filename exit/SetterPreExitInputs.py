import pandas as pd
import multiprocessing
from commonudm.GetterStockQtn import getterStockQtn
import xlwings as xw


def setterPreExitInputs(lock=multiprocessing.Lock()):
    lock.acquire()
    n = getterStockQtn()
    lock.release()
    df = pd.DataFrame(columns=["id", 'rFlag', 'eFlag'], index=list(range(n)))
    df[:] = 0
    df['id'] = list(range(1, n + 1))
    lock.acquire()
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv",
        index=False)
    lock.release()
    while True:
        try:
            with lock:
                wb = xw.Book(
                    "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
                dt = wb.sheets("ExitInput")
                dt.range(f"a1:c{n + 1}").options(pd.DataFrame, index=False).value = df
            break
        except Exception as e:
            print(f"The exception while setterPreExitInputs is {e}")


# setterPreExitInputs()
