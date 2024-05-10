import pandas as pd
import xlwings as xw
from commonudm.GetterStockQtn import getterStockQtn


def setterNiftyDetailedListWithPivot(sheetName="nifty500"):
    while True:
        try:
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            n = getterStockQtn()
            # getting dataframe
            dt = wb.sheets(sheetName)
            df = pd.DataFrame(dt.range(f"a1:u{n+1}").value)
            break
        except Exception as e:
            print(f"Exception while getterPrePortfolio is {e}")
    df.columns = df.iloc[0]
    df = df[1:]
    df["id"] = df["id"].astype("int64")
    df["token"] = df["token"].astype("int64")
    df.index = list(range(n))
    df = df.loc[:, ['id', 'sector', 'symbol', 'token', 'C']]
    # here PC is previous intraday close price
    df.rename(columns={'C': 'PC'}, inplace=True)
    df.to_csv(
        "F:\\AT\\commonudm\\resource\\NiftyDetailedListWithPivots.csv",
        index=False)
    return df


# setterNiftyDetailedListWithPivot()
