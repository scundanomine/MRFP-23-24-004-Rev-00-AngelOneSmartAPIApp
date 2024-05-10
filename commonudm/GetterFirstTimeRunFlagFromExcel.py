import pandas as pd
import xlwings as xw
from commonudm.GetterReportDateForRR import getterReportDateForRR
from position.GetterPositionIdForSpecificDate import getterPositionIdForSpecificDate


def getterFirstTimeRunFlagFromExcel():
    reportDate = getterReportDateForRR()
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            flagF = dt['T2'].value
            if flagF is None or flagF == "T":
                flagF = 'F'
                dt['T2'].value = 'F'
                dt['O2'].value = 0
                marDf = pd.DataFrame([0], columns=['pid'])
                marDf.to_csv(
                    f"F:\\AT\\report\\media\\{reportDate}\\state\\PId.csv",
                    index=False)
            else:
                pid = getterPositionIdForSpecificDate(reportDate)
                dt['O2'].value = pid
            break
        except Exception as e:
            print(f"Exception while getterPreStockQtn is {e}")
    return flagF


# print(getterFirstTimeRunFlagFromExcel())
