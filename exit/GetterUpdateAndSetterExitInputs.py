import pandas as pd
import xlwings as xw
from commonudm.GetterStockQtn import getterStockQtn


def getterUpdateAndSetterExitInputs(row, lock):
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv")
        uid = row[0]
        df.iloc[uid - 1] = row
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv",
            index=False)
        wb = xw.Book(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
        dt = wb.sheets("ExitInput")
        lock.acquire()
        n = getterStockQtn()
        dt.range(f"a1:c{n+1}").options(pd.DataFrame, index=False).value = df
        lock.release()
    except Exception as e:
        print(f"The exception while getter, update and setter exit input list is {e}")
