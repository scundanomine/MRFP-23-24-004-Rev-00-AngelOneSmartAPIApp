import pandas as pd
import xlwings as xw


def getSmallData():
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("Exchange")
    varS = pd.DataFrame(dt.range("a1:l202").value)
    varS.columns = varS.iloc[0]
    varS = varS[1:]
    varS["id"] = varS["id"].astype("int64")
    varS["token"] = varS["token"].astype("int64")
    varS = varS.drop(columns=['symbol', 'token'])
    return varS


# print(getSmallData())
