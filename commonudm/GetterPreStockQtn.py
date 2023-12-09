import pandas as pd
import xlwings as xw


def getterPreStockQtn():
    # getting data from the sheet
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    # MAndP is margin and portfolio list
    dt = wb.sheets("MAndP")

    # creating the df
    marDf = pd.DataFrame(dt.range("k2:k3").value)
    marDf.rename(columns={0: 'stockQtn'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf = marDf.astype("int64")
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\StockQtn.csv",
        index=False)
    return marDf
