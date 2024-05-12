import pandas as pd
import xlwings as xw


def getterPrePositionId():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")

            # creating the df
            marDf = pd.DataFrame([dt['O2'].value], columns=['pid'])
            break
        except Exception as e:
            print(f"Exception while getterPrePositionId is {e}")
    if marDf.loc[0, 'pid'] is None:
        marDf.loc[0, 'pid'] = 0
    marDf = marDf.astype("int64")
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PId.csv",
        index=False)
    return marDf


# print(getterPrePositionId())
