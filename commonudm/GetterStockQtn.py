import pandas as pd
from commonudm.GetterPreStockQtn import getterPreStockQtn


def getterStockQtn():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\StockQtn.csv")
    except Exception as e:
        print(f"The exception while getter stock qtn is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterPreStockQtn()
    # return df['exitTime'][0]
    return df['stockQtn'][0]


# print(getterStockQtn())
