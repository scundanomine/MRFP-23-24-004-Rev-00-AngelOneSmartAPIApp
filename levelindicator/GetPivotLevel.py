import pandas as pd
import xlwings as xw


def getPivotLevelData():
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("Exchange")
    varP = pd.DataFrame(dt.range("a1:l202").value)
    varP.columns = varP.iloc[0]
    varP = varP[1:]
    varP["id"] = varP["id"].astype("int64")
    varP = varP.drop(columns=['symbol', 'token'])
    return varP
