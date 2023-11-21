import xlwings as xw
import time
import pandas as pd


def getCustomDfBlackListET(sheetName, ect=2):
    # startT = time.time()
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets(sheetName)
    dataList = dt.range(f"a{ect}:a50").value

    upperBound = 0
    ctr = 2
    for result in dataList:
        if result is None:
            upperBound = ctr - 1
            break
        ctr = ctr + 1

    df = pd.DataFrame(dt.range(f"a{ect}:b{upperBound}").value, columns=["id", 'bFlag'])
    df["id"] = df["id"].astype("int64")
    # print(f"time of execution is {time.time() - startTime}")
    return df


# print(getCustomDfBlackListET("BlackList"))
