import pandas as pd
import xlwings as xw


def getterReportPreDate():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")

            # creating the df
            marDf = pd.DataFrame([dt['Q2'].value], columns=['date'])
            break
        except Exception as e:
            print(f"Exception while getterPrePositionId is {e}")
    marDf.to_csv(
        "F:\\AT\\report\\areportstate\\date.csv",
        index=False)
    return marDf


# print(getterReportPreDate())
