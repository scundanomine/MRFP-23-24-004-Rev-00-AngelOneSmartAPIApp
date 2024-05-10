import pandas as pd
import xlwings as xw


def getterPreLiveStatus():
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")

            # creating the df
            marDf = pd.DataFrame(dt.range("O2:O3").value)
            isLive = dt['O2'].value
            break
        except Exception as e:
            print(f"Exception while getterPreLiveStatus is {e}")
    marDf.rename(columns={0: 'isLive'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf.to_csv(
        "F:\\AT\\commonudm\\resource\\LiveStatus.csv",
        index=False)
    return eval(isLive)


# print(type(getterPreLiveStatus()))
# print(getterPreLiveStatus())
