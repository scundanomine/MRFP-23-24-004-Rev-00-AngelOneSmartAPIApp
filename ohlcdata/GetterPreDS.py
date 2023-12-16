import pandas as pd
from commonudm.GetterStockQtn import getterStockQtn


def getterPreDS():
    n = getterStockQtn()
    df = pd.DataFrame(columns=[0, 1, 2, 3, 4, 5], index=list(range(n)))
    df[:] = 0
    return df


# print(getterFDS())
