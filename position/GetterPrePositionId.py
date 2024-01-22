import pandas as pd
import xlwings as xw
import multiprocessing


def getterPrePositionId(lock=multiprocessing.Lock()):
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")

            # creating the df
            marDf = pd.DataFrame(dt.range("O2:O3").value)
            break
        except Exception as e:
            print(f"Exception while getterPrePositionId is {e}")
    marDf.rename(columns={0: 'pid'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf = marDf.astype("int64")
    lock.acquire()
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PId.csv",
        index=False)
    lock.release()
    return marDf


# getterPrePositionId()
