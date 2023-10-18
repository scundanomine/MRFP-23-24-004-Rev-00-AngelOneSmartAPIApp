import pandas as pd
import xlwings as xw


def getSymbolAndToken():
    cdf = pd.read_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\SymbolAndToken.csv")
    return cdf


# print(getSymbolAndToken())
