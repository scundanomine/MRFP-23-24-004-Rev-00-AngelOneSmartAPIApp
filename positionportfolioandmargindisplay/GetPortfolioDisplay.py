import xlwings as xw
import pandas as pd
from portfolio.GetterFixedPortfolio import getterFixedPortfolio
from position.GetterPositionList import getterPositionList


def getPortfolioDisplay(lock):
    df = getterFixedPortfolio(lock)
    pLDf = getterPositionList(lock)
    portfolio = df.loc[0, 'portfolio']
    try:
        portfolio = portfolio + pLDf['gol'].sum()
    except Exception as e:
        print(f"Exception while calculating getPortfolioDisplay is {e}")
        return
    while True:
        try:
            with lock:
                wb = xw.Book(
                    "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
                # MAndP is margin and portfolio list
                dt = wb.sheets("MAndP")
                dt['C2'].value = portfolio
            break
        except Exception as e:
            print(f"Exception while getPortfolioDisplay is {e}")
