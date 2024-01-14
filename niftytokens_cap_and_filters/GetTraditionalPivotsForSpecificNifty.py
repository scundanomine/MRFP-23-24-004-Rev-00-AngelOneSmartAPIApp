from concurrent.futures import ThreadPoolExecutor
from AngelOneSmartAPIApp.GetLiveData import *
from AngelOneSmartAPIApp.HistoricDataForOneDayForTraditionalPivot import historicDataForOneDayForTraditionalPivot
from commonudm.SetterNiftyDetailedListWithPivots import setterNiftyDetailedListWithPivot

df = pd.DataFrame()
n = 0
obj = []


def getTraditionalPivotsForSpecificNiftyFile(sheetName, upperBound, refDate, objC=0):
    global df, n, obj
    startTime = time.time()

    # obj = objC
    while True:
        try:
            obj, accessToken = get_access_token()
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting dataframe
    dt = wb.sheets(sheetName)
    df = pd.DataFrame(dt.range(f"d2:u{upperBound}").value)
    df.rename(
        columns={0: "symbol", 1: "token", 2: "cap", 3: "O", 4: "H", 5: "L", 6: "C", 7: "s5", 8: "s4", 9: "s3", 10: "s2",
                 11: "s1", 12: "p", 13: "r1", 14: "r2", 15: "r3", 16: "r4", 17: "r5"}, inplace=True)
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
            data = historicDataForOneDayForTraditionalPivot(obj, refDate, str(df["token"][r]))[0]
            # print(data)
            # df.loc[r, "ltp"] = data["ltp"]
            opn = data[1]
            high = data[2]
            low = data[3]
            close = data[4]

            if opn is None:
                opn = 0
                high = 0
                low = 0
                close = 0

            # setting ohlc data
            df.loc[r, "O"] = opn
            df.loc[r, "H"] = high
            df.loc[r, "L"] = low
            df.loc[r, "C"] = close

            # setting pivots data
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
    for i in range(3, n + 2 * 3 - n % 3, 3):
        time.sleep(1)
        with ThreadPoolExecutor() as executor:
            lt = list(range(i - 3, i))
            executor.map(getTraditionalPivots, lt)

    # render data back to excel
    df = df.drop(columns=["symbol", "token"])
    print(df)
    dt.range(f"g1:u{upperBound}").options(pd.DataFrame, index=False).value = df
    setterNiftyDetailedListWithPivot()
    print(f"execution time is {time.time() - startTime}")


getTraditionalPivotsForSpecificNiftyFile("nifty500", "502", "2024-01-09")
