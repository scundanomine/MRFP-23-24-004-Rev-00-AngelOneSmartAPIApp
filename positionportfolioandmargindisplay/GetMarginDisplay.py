import xlwings as xw
import pandas as pd
from margin.GetterAvailableMargin import getterAvailableMargin


def getMarginDisplay(lock):
    df = getterAvailableMargin(lock)
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            dt.range("a2:a3").options(pd.DataFrame, index=False).value = df
            break
        except Exception as e:
            print(f"Exception while getMarginDisplay is {e}")
