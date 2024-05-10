import pandas as pd
import xlwings as xw


def getterPreTimeDelta():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            marDf = pd.DataFrame(dt.range("i2:i3").value)
            break
        except Exception as e:
            print(f"Exception while getterPreTimeDelta: {e}")
    marDf.rename(columns={0: 'timeDelta'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf.to_csv(
        "F:\\AT\\commonudm\\resource\\TimeDelta.csv",
        index=False)
    return marDf


# getterPreTimeDelta()
