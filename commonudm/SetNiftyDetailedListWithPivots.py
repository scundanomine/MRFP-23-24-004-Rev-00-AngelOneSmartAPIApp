import pandas as pd
import xlwings as xw


def setNiftyDetailedListWithPivot(sheetName="nifty500"):
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting dataframe
    dt = wb.sheets(sheetName)
    df = pd.DataFrame(dt.range(f"a1:u{502}").value)
    df.columns = df.iloc[0]
    df = df[1:]
    df["id"] = df["id"].astype("int64")
    df.index = list(range(501))
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\NiftyDetailedListWithPivots.csv",
        index=False)


# setNiftyDetailedListWithPivot()
