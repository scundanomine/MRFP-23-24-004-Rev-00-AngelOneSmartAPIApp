import pandas as pd
import xlwings as xw


def getterPreReferenceTime():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            marDf = pd.DataFrame([dt['E2'].value], columns=['refTime'])
            break
        except Exception as e:
            print(f"Exception while getting pre ref time: {e}")
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\RefTime.csv",
        index=False)
    return marDf


# getterPreReferenceTime()
