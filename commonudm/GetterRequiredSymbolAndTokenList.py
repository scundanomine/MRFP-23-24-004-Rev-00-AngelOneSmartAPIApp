import pandas as pd
from commonudm.SetterRequiredSymbolAndTokenList import setterRequiredSymbolAndTokenList


def getterRequiredSymbolAndTokenList():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\RequiredSymbolAndToken.csv")
    except Exception as e:
        print(f"Exception while getterRequiredSymbolAndTokenList is {e}")
        df = getterRequiredSymbolAndTokenList()

    return df


# print(getterRequiredSymbolAndTokenList())
