import pandas as pd
import xlwings as xw
import multiprocessing


def getterPreMargin(lock=multiprocessing.Lock()):
    # getting data from the sheet
    while True:
        try:
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            marDf = pd.DataFrame(dt.range("a2:a3").value)
            break
        except Exception as e:
            print(f"Exception while getterPreMargin is {e}")
    marDf.rename(columns={0: 'margin'}, inplace=True)
    marDf = marDf.drop(labels=[1], axis=0)
    marDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv",
        index=False)
    return marDf


# getterPreMargin()
