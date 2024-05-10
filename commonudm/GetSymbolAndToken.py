import pandas as pd


def getSymbolAndToken():
    try:
        cdf = pd.read_csv(
            "F:\\AT\\commonudm\\resource\\SymbolAndToken.csv")
    except Exception as e:
        print(f"Exception while getSymbolAndToken is {e}")
        cdf = getSymbolAndToken()
    return cdf


# print(getSymbolAndToken())
