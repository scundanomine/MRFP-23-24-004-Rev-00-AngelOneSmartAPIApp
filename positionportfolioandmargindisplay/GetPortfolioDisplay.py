import xlwings as xw
import pandas as pd
from portfolio.GetterFixedPortfolio import getterFixedPortfolio
from position.GetterPositionList import getterPositionList


def getPortfolioDisplay(lock):
    df = getterFixedPortfolio(lock)
    pLDf = getterPositionList(lock)
    try:
        df.loc[0, 'portfolio'] = df.loc[0, 'portfolio'] + pLDf['gol'].sum()
    except:
        return
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            # dt.range("c1:c2").options(pd.DataFrame, index=False).value = df
            lock.acquire()
            dt['C2'].value = df.loc[0, 'portfolio']
            lock.release()
            break
        except Exception as e:
            print(f"Exception while getPortfolioDisplay is {e}")
