import pandas as pd
import xlwings as xw


def getSRData():
    # getting data from the sheet
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("nifty500")

    # creating the df
    varSR = pd.DataFrame(dt.range("a1:u501").value)
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
    # varSR["token"] = varSR["token"].astype("int64")
    # varSR = varSR.drop(columns=['symbol', 'token'])

    # rename the column
    varSR.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    return varSR


# print(getSRData())
