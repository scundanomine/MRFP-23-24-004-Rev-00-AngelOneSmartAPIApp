import pandas as pd
import xlwings as xw
import multiprocessing


def getterPreStockQtn():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            qt = dt['K2'].value
            marDf = pd.DataFrame([qt])
            break
        except Exception as e:
            print(f"Exception while getterPreStockQtn is {e}")
    marDf.rename(columns={0: 'stockQtn'}, inplace=True)
    if marDf.loc[0, 'stockQtn'] is not None:
        marDf['stockQtn'] = marDf['stockQtn'].astype("int64")
    else:
        marDf.loc[0, 'stockQtn'] = 120
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\StockQtn.csv",
        index=False)
    return marDf


# print(getterPreStockQtn())