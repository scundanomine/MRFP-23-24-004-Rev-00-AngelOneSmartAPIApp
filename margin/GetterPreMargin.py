import pandas as pd
import xlwings as xw


def getterPreMargin():
    # getting data from the sheet
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("margin")

    # creating the df
    marDf = pd.DataFrame(dt.range("a2:a3").value)
    marDf.rename(columns={0: 'margin'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv",
        index=False)
    return marDf
