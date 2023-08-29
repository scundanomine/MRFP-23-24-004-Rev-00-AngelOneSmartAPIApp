import json
import pandas as pd
import xlwings as xw


def getToken():
    with open(f"OpenAPIScripMaster.json", "r") as f:
        bigData = json.load(f)
    varBig = pd.DataFrame(bigData, columns=["token", "symbol"])
    # print(varBig)

    wb = xw.Book("TA_Python.xlsm")
    dt = wb.sheets("Sheet2")

    smallData = dt.range("g2:g202").value
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
    dt.range("f1:f202").value = varSmall["token"]


getToken()
