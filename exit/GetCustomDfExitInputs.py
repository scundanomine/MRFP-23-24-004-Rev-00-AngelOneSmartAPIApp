import pandas as pd
import xlwings as xw
from commonudm.GetterStockQtn import getterStockQtn


def getCustomDfExitInputs():
    # startTime = time.time()
    while True:
        try:
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("ExitInput")
            n = getterStockQtn()
            df = pd.DataFrame(dt.range(f"a{2}:c{n+1}").value, columns=["id", 'rFlag', 'eFlag'])
            df = df.astype("int64")
            if dt['Q2'].value == 1:
                df.to_csv(
                    "F:\\AT\\exit\\exitstate\\ExitInputs.csv",
                    index=False)
                dt['Q2'].value = 0
            break
        except Exception as e:
            print(f"Exception while getCustomDfExitInputs is {e}")
    return df


# print(getCustomDfExitInputs())
