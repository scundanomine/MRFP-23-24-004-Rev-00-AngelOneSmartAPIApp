import pandas as pd
from commonudm.GetterPreStockQtn import getterPreStockQtn


def getterMarketStructureDf():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv")
    except Exception as e:
        print(f"The exception while getterMarketStructureDf is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterMarketStructureDf()
    return df


# print(getterStockQtn())
