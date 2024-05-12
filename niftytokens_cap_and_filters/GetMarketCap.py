import pandas as pd
import xlwings as xw
import time


def getMarketCap(smallDataSheetName, smallDataUpperBound):
    startTime = time.time()
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting big dataframe
    dtBig = wb.sheets("MarketCap")
    bigData = pd.DataFrame(dtBig.range("b2:d2014").value)
    bigData = bigData.drop(columns=[1])
    bigData.rename(columns={2: 1}, inplace=True)
    bigData[1] = bigData[1].astype("int64")
    print(bigData)

    # getting small dataframe
    dtSmall = wb.sheets(smallDataSheetName)
    rangeS = f"d2:f{smallDataUpperBound}"
    smallData = pd.DataFrame(dtSmall.range(rangeS).value)
    smallData = smallData.drop(columns=[1])
    smallData.rename(columns={2: "cap"}, inplace=True)
    print(smallData)

    # get data using nested loop
    for i in range(len(smallData)):
        for j in range(len(bigData)):
            if smallData[0][i] == f"{bigData[0][j]}-EQ":
                smallData.loc[i, "cap"] = bigData[1][j]
                break
    smallData = smallData.drop(columns=[0])

    # render data to the excel
    dtSmall.range(f"f1:f{smallDataUpperBound}").options(pd.DataFrame, index=False).value = smallData
    print(f"execution time is {time.time() - startTime}")


getMarketCap("nifty500", "502")
