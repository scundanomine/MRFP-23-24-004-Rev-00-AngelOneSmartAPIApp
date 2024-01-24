from commonudm.GetSymbolAndToken import getSymbolAndToken


def getListOfTokensForSpecificNumber(n1, n2):
    # getter symbol and token
    df = getSymbolAndToken()
    tokList = df['token'].tolist()
    lst = tokList[n1:n2]
    return lst


# print(getListOfTokensForSpecificNumber(30, 60))
