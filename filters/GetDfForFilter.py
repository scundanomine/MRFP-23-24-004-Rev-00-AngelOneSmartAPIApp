import pandas as pd
import xlwings as xw


def getDfForFilter(sheetName, upperBound):
    wb = xw.Book(
        "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets(sheetName)
    df = pd.DataFrame(dt.range(f"a1:u{upperBound}").value)
    df.columns = df.iloc[0]
    df = df[1:]
    # above means it will only take columns from 1 to m
    idx = list(range(len(df["id"])))
    df = df.set_index(pd.Index(idx))
    df["id"] = df["id"].astype("int64")
    df["token"] = df["token"].astype("int64")
    df["cap"] = df["cap"].astype("int64")
    # df = df.drop(columns=['symbol', 'token'])
    return df
