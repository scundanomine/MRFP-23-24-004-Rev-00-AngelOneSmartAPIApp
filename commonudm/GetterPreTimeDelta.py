import pandas as pd
import xlwings as xw


def getterPreTimeDelta():
    # getting data from the sheet
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    # MAndP is margin and portfolio list
    dt = wb.sheets("MAndP")

    # creating the df
    marDf = pd.DataFrame(dt.range("i2:i3").value)
    marDf.rename(columns={0: 'timeDelta'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\TimeDelta.csv", index=False)
    return marDf
