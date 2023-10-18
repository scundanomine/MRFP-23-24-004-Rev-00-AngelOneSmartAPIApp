import pandas as pd
import xlwings as xw


def getSRData():
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("nifty500")
    varSR = pd.DataFrame(dt.range("a1:u202").value)
    varSR.columns = varSR.iloc[0]
    varSR = varSR[1:]
    # above means it will only take columns from 1 to m
    idx = list(range(len(varSR["id"])))
    varSR = varSR.set_index(pd.Index(idx))
    varSR["id"] = varSR["id"].astype("int64")
    varSR["token"] = varSR["token"].astype("int64")
    # varSR = varSR.drop(columns=['symbol', 'token'])
    return varSR


# print(getSRData())
