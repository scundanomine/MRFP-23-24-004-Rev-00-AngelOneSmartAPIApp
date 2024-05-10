import pandas as pd
import xlwings as xw
import time


def sortSpecificNiftySheet(sheetName, upperBound):
    startTime = time.time()
    wb = xw.Book(
        "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting dataframe
    dt = wb.sheets(sheetName)
    df = pd.DataFrame(dt.range(f"b2:f{upperBound}").value)
    df.rename(columns={0: "disc", 1: "sector", 2: "symbol", 3: "token", 4: "cap"}, inplace=True)
    df["token"] = df["token"].astype("int64")
    df["cap"] = df["cap"].astype("int64")
    print(df)

    # logic for logic
    df.sort_values(by=['cap'], inplace=True, ascending=False)
    print(df)

    # Render data back to the excel
    dt.range(f"b1:f{upperBound}").options(pd.DataFrame, index=False).value = df
    print(f"execution time is {time.time() - startTime}")


sortSpecificNiftySheet("nifty500", "502")
