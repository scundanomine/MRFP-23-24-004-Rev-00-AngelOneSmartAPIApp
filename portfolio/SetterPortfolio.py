import xlwings as xw
import pandas as pd


def setterPortfolio(df, lock):
    while True:
        try:
            wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            lock.acquire()
            dt.range("c1:c2").options(pd.DataFrame, index=False).value = df
            lock.release()
            break
        except Exception as e:
            print(f"Exception while getterPrePortfolio is {e}")
    lock.acquire()
    df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\portfolio.csv", index=False)
    lock.release()
