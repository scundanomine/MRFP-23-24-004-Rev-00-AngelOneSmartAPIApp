import pandas as pd
import xlwings as xw


def getSmallData():
    wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets("Exchange")
    varS = pd.DataFrame(dt.range("a1:m202").value)
    varS.columns = varS.iloc[0]
    varS = varS[1:]
    varS["id"] = varS["id"].astype("int64")
    varS["token"] = varS["token"].astype("int64")
    varS = varS.drop(columns=['symbol', 'sector', 'token'])
    return varS


# print(getSmallData())
