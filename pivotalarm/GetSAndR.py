import pandas as pd
import xlwings as xw


def getSRData():
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("Exchange")
    varSR = pd.DataFrame(dt.range("a1:l202").value)
    varSR.columns = varSR.iloc[0]
    varSR = varSR[1:]
    varSR["id"] = varSR["id"].astype("int64")
    # varSR = varSR.drop(columns=['symbol', 'token'])
    return varSR
