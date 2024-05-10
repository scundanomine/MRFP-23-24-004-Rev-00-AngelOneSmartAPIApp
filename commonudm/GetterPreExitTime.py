import pandas as pd
import xlwings as xw


def getterPreExitTime():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")

            # creating the df
            marDf = pd.DataFrame(dt.range("g2:g3").value)
            break
        except Exception as e:
            print(f"Exception while getterPreExitTime is {e}")
    marDf.rename(columns={0: 'exitTime'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf.to_csv(
        "F:\\AT\\commonudm\\resource\\ExitTime.csv", index=False)
    return marDf
