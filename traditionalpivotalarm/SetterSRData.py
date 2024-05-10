import pandas as pd
import xlwings as xw
from commonudm.GetterStockQtn import getterStockQtn


def setterSRData():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("nifty500")
            n = getterStockQtn()
            # creating the df
            varSR = pd.DataFrame(dt.range(f"a1:u{n+1}").value)
            break
        except Exception as e:
            print(f"Exception while setterSRData is {e}")
    varSR.columns = varSR.iloc[0]
    varSR = varSR[1:]
    # above means it will only take columns from 1 to m

    # setting index
    idx = list(range(len(varSR["id"])))
    varSR = varSR.set_index(pd.Index(idx))

    # dropping unnecessary columns
    varSR = varSR.drop(columns=["disc", "sector", "symbol", "token", "cap", "O", "H", "L"])

    # adding new column to df
    varSR.insert(2, "bigS", 0)
    varSR.insert(14, "bigM", 200000)

    varSR["id"] = varSR["id"].astype("int64")

    # rename the column
    varSR.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    varSR.to_csv("F:\\AT\\traditionalpivotalarm\\pivotstate\\SRData.csv", index=False)

    return varSR


# print(setterSRData())
