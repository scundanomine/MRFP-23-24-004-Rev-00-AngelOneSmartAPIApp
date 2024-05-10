import xlwings as xw
import pandas as pd
from commonudm.GetterStockQtn import getterStockQtn


def getCustomDfBlackListET():
    while True:
        try:
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("BlackList")
            n = getterStockQtn()
            df = pd.DataFrame(dt.range(f"a{2}:b{n+1}").value, columns=["id", 'bFlag'])
            df["id"] = df["id"].astype("int64")
            df["bFlag"] = df["bFlag"].astype("int64")
            break
        except Exception as e:
            print(f"Exception while getCustomDfBlackListET is {e}")
    return df


# print(getCustomDfBlackListET())
