import pandas as pd


def getSymbolAndToken():
    try:
        cdf = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\SymbolAndToken.csv")
    except Exception as e:
        print(f"Exception while getSymbolAndToken is {e}")
        cdf = getSymbolAndToken()
    return cdf


# print(getSymbolAndToken())
