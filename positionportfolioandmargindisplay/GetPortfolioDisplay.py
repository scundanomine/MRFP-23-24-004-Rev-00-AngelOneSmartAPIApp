import xlwings as xw
from portfolio.GetterFixedPortfolio import getterFixedPortfolio
from position.GetterPositionList import getterPositionList


def getPortfolioDisplay():
    df = getterFixedPortfolio()
    pLDf = getterPositionList()
    portfolio = df.loc[0, 'portfolio']
    try:
        df.loc[0, 'portfolio'] = df.loc[0, 'portfolio'] + pLDf['gol'].sum()
        df.to_csv('E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\CurrentPortfolio.csv', index=False)
    except Exception as e:
        print(f"Exception while calculating getPortfolioDisplay is {e}")
        return
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            dt['C2'].value = df.loc[0, 'portfolio']
            break
        except Exception as e:
            print(f"Exception while getPortfolioDisplay is {e}")
