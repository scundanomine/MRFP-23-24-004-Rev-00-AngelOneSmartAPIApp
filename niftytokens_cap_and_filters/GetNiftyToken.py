import json
import pandas as pd
import xlwings as xw
import time
import math
from concurrent.futures import ThreadPoolExecutor

varBig = []
smallData = []


def getNiftyToken(sheetName):
    global varBig, smallData
    startTime = time.time()
    with open(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\niftytokens\\OpenAPIScripMaster.json",
            "r") as f:
        bigData = json.load(f)
    varBig = pd.DataFrame(bigData, columns=["token", "symbol"])
    n = math.floor(pow(len(varBig["token"]), 0.5))
    # print(n)
    # print(varBig)

    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets(sheetName)

    smallData = dt.range("d2:d502").value
    x = {"symbol": smallData}
    varSmall = pd.DataFrame(x)
    varSmall["token"] = varSmall["symbol"]
    # print(varSmall)

    for i in range(len(varSmall)):
        for j in range(len(varBig)):
            if varSmall["symbol"][i] == varBig["symbol"][j]:
                varSmall["token"][i] = varBig["token"][j]
                break

    # dt.range("c2:c202").value =
    # print(varSmall)
    dt.range("e1:e502").value = varSmall["token"]
    print(f"Execution time is {time.time() - startTime}")


getNiftyToken("nifty500")
