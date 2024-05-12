from commonudm.GetSymbolAndToken import getSymbolAndToken
from commonudm.GetterStockQtn import getterStockQtn


def setterRequiredSymbolAndTokenList():
    gDf = getSymbolAndToken()

    n = getterStockQtn()
    # delete all row except n and column except few
    dfSize = len(gDf)
    gDf = gDf.drop(labels=range(n, dfSize), axis=0)
    gDf = gDf.loc[:, ['id', 'symbol', 'token']]
    gDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\RequiredSymbolAndToken.csv",
        index=False)


# setterRequiredSymbolAndTokenList()
