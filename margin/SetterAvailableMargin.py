import xlwings as xw
import pandas as pd
import multiprocessing


def setterAvailableMargin(df, lock=multiprocessing.Lock()):
    while True:
        try:
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            lock.acquire()
            dt.range("a1:a2").options(pd.DataFrame, index=False).value = df
            lock.release()
            break
        except Exception as e:
            print(f"Exception while setterAvailableMargin is {e}")
    lock.acquire()
    df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv", index=False)
    lock.release()