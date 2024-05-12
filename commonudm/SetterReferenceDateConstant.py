import datetime
import xlwings as xw
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterReferenceTime import getterReferenceTime
import pandas as pd


def setterReferenceDateConstant():
    getterPreReferenceTime()
    dateR = getterReferenceTime()
    refDate = datetime.datetime.strptime(dateR, "%d %b %Y %H:%M:%S.%f")
    c = datetime.datetime.now() - refDate
    while True:
        try:
            # setter to excell and df
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            dt["I2"].value = str(c)
            break
        except Exception as e:
            print(f"Exception while setterReferenceDateConstant is {e}")

    marDf = pd.DataFrame([str(c)], columns=['timeDelta'])
    # marDf = marDf.drop(labels=[1], axis=0)
    # marDf.loc[0, 'timeDelta'] = str(c)
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\TimeDelta.csv",
        index=False)


# setterReferenceDateConstant()
