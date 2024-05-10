import pandas as pd
from commonudm.GetSymbolAndToken import getSymbolAndToken


def getListOfTokensForWebsocket(N=0, n=0):
    # getter symbol and token
    df = getSymbolAndToken()
    tokList = df['token'].tolist()
    r = int(N / n)
    for i in range(n):
        lst = tokList[i * r:(i + 1) * r]
        ds = pd.Series(lst)
        ds.to_csv(
            f"F:\\AT\\smartwebsocketdata\\websocketstate\\tokenlist\\TokenList{i}.csv",
            index=False)


# getListOfTokensForWebsocket(120, 2)
