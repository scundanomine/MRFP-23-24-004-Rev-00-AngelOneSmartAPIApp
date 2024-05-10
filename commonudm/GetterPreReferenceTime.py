import pandas as pd
import xlwings as xw


def getterPreReferenceTime():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            marDf = pd.DataFrame([dt['E2'].value], columns=['refTime'])
            break
        except Exception as e:
            print(f"Exception while getting pre ref time: {e}")
    marDf.to_csv(
        "F:\\AT\\commonudm\\resource\\RefTime.csv",
        index=False)
    return marDf


# getterPreReferenceTime()
