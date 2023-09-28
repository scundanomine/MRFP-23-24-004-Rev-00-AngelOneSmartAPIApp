import time
import pandas as pd
import xlwings as xw
from concurrent.futures import ThreadPoolExecutor
from AngelOneSmartAPIApp.GetLiveData import *
from AngelOneSmartAPIApp.HistoricDataForOneDay import *

df = pd.DataFrame()
n = 0
obj = []


def getTraditionalPivotsForSpecificNiftyFile(sheetName, upperBound):
    global df, n, obj
    startTime = time.time()

    obj, toc = get_access_token()

    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting dataframe
    dt = wb.sheets(sheetName)
    df = pd.DataFrame(dt.range(f"d2:r{upperBound}").value)
    df.rename(columns={0: "symbol", 1: "token", 2: "cap", 3: "ltp", 4: "s5", 5: "s4", 6: "s3", 7: "s2", 8: "s1", 9: "p",
                       10: "r1", 11: "r2", 12: "r3", 13: "r4", 14: "r5"}, inplace=True)
    df["token"] = df["token"].astype("int64")
    df = df.drop(columns=["cap"])
    results = []
    n = len(df)

    # define function for executor
    def getTraditionalPivots(r):
        global df, n, obj
        if r > n - 1:
            return
        else:
            # get past data
            data = getHistoricDataForOneDay(obj, "2023-09-27", str(df["token"][r]))
            # print(data)
            # df.loc[r, "ltp"] = data["ltp"]
            high = data[2]
            low = data[3]
            close = data[4]
            median = (high + low + close) / 3
            df.loc[r, "p"] = median
            df.loc[r, "r1"] = median * 2 - low
            df.loc[r, "s1"] = median * 2 - high
            df.loc[r, "r2"] = median + 1 * (high - low)
            df.loc[r, "s2"] = median - 1 * (high - low)
            df.loc[r, "r3"] = median * 2 + (high - 2 * low)
            df.loc[r, "s3"] = median * 2 - (2 * high - low)
            df.loc[r, "r4"] = median * 3 + (high - 3 * low)
            df.loc[r, "s4"] = median * 3 - (3 * high - low)
            df.loc[r, "r5"] = median * 4 + (high - 4 * low)
            df.loc[r, "s5"] = median * 4 - (4 * high - low)

    # Logic of magic no '3, n + 2 * 3 - n % 3, 3'
    for i in range(3, 50 + 2 * 3 - 50 % 3, 3):
        time.sleep(1)
        with ThreadPoolExecutor() as executor:
            lt = list(range(i - 3, i))
            executor.map(getTraditionalPivots, lt)

    # render data back to excel
    df = df.drop(columns=["symbol", "token"])
    print(df)
    dt.range(f"g1:r{upperBound}").options(pd.DataFrame, index=False).value = df
    print(f"execution time is {time.time() - startTime}")


getTraditionalPivotsForSpecificNiftyFile("nifty500", "502")
