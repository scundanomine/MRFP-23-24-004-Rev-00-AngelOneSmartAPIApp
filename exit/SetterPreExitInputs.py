import pandas as pd
import xlwings as xw
from commonudm.GetterStockQtn import getterStockQtn


def setterPreExitInputs():
    n = getterStockQtn()
    df = pd.DataFrame(columns=["id", 'rFlag', 'eFlag'], index=list(range(n)))
    df[:] = 0
    df['id'] = list(range(1, n + 1))
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv",
        index=False)
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("ExitInput")
            dt.range(f"a1:c{n + 1}").options(pd.DataFrame, index=False).value = df
            break
        except Exception as e:
            print(f"The exception while setterPreExitInputs is {e}")


# setterPreExitInputs()
