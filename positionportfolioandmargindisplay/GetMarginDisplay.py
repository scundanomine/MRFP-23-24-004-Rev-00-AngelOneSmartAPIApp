import xlwings as xw
import pandas as pd
from margin.GetterAvailableMargin import getterAvailableMargin


def getMarginDisplay():
    df = getterAvailableMargin()
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            # dt.range("a1:a2").options(pd.DataFrame, index=False).value = df
            dt['A2'].value = df.loc[0, 'margin']
            break
        except Exception as e:
            print(f"Exception while getMarginDisplay is {e}")
