import xlwings as xw
import pandas as pd


def setterPortfolio(df):
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    # MAndP is margin and portfolio list
    dt = wb.sheets("MAndP")
    dt.range("c1:c2").options(pd.DataFrame, index=False).value = df
    df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\portfolio.csv", index=False)
