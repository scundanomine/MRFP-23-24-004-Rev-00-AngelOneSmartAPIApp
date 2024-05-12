import datetime
import xlwings as xw
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterReferenceTime import getterReferenceTime
import pandas as pd


def setterReportDateForRR():
    getterPreReferenceTime()
    dateR = getterReferenceTime()
    c = datetime.datetime.strptime(dateR, "%d %b %Y %H:%M:%S.%f").strftime("%Y-%m-%d")
    while True:
        try:
            # setter to excell and df
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            dt["Q2"].value = str(c)
            break
        except Exception as e:
            print(f"Exception while setterReportDate is {e}")

    marDf = pd.DataFrame([str(c)], columns=['rDate'])
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\ReportDate.csv",
        index=False)


# setterReportDate()
