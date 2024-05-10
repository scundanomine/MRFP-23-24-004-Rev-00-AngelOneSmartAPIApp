import pandas as pd
from commonudm.GetterPreStockQtn import getterPreStockQtn


def getterStockQtn():
    try:
        df = pd.read_csv(
            "F:\\AT\\commonudm\\resource\\StockQtn.csv")
    except Exception as e:
        print(f"The exception while getter stock qtn is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterStockQtn()
    return df['stockQtn'][0]


# print(getterStockQtn())
