import pandas as pd
from commonudm.SetterRequiredSymbolAndTokenList import setterRequiredSymbolAndTokenList


def getterRequiredSymbolAndTokenList():
    try:
        df = pd.read_csv(
            "F:\\AT\\commonudm\\resource\\RequiredSymbolAndToken.csv")
    except Exception as e:
        print(f"Exception while getterRequiredSymbolAndTokenList is {e}")
        df = getterRequiredSymbolAndTokenList()

    return df


# print(getterRequiredSymbolAndTokenList())
