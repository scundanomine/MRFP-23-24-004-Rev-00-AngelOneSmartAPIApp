import pandas as pd
from commonudm.SetterRequiredSymbolAndTokenList import setterRequiredSymbolAndTokenList


def getterRequiredSymbolAndTokenList():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\RequiredSymbolAndToken.csv")
    except Exception as e:
        print(f"The exception while required symbol and token list is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        setterRequiredSymbolAndTokenList()
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\RequiredSymbolAndToken.csv")

    return df


# print(getterAvailableMargin())
