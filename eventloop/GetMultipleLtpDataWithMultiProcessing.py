from concurrent.futures import ProcessPoolExecutor
import time
import pandas as pd
from commonudm.GetSymbolAndToken import *
import math
from AngelOneSmartAPIApp.test import *

dfm = pd.DataFrame()
m = 500
p = 100
i = 0
objOneX = []
objTwoX = []
exchange = "NSE"


def getAccessTokenWithThread(r, lock=""):
    startTime = time.time()
    global objOneX, objTwoX, dfm, p, i
    dfm = getSymbolAndToken()
    ds = pd.Series(index=list(range(100)))
    dtc = []
    ctr = 20

    # data instance for excel
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting big dataframe
    dtc = wb.sheets("Sheet1")
    # creating session one
    while True:
        try:
            objOneX, accessTokenOneX = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    # creating session two
    while True:
        try:
            objTwoX, accessTokenOneX = getAccessTokenOne("F5SzrULj", "S53761277", "8813", "2NF7QBQP7R3NEDXC4VN6UNWYWM")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    def getLtpE(uid):
        time.sleep(0.001)
        global objOneX, objTwoX, dfm, i
        a = dfm["symbol"][uid]
        b = dfm["token"][uid]
        if uid < i - 10:
            try:
                ltp = objOneX.ltpData(exchange, a, str(b))['data']['ltp']
            except:
                ltp = 0
        else:
            try:
                ltp = objTwoX.ltpData(exchange, a, str(b))['data']['ltp']
            except:
                ltp = 0
        # dfm.loc[uid, "ltp"] = ltp['data']['ltp']
        return ltp

    # main loop for thread
    ctrA = 0
    while 50 - (time.time() - startTime) > 0:
        ds[:] = 0
        ctr = 20
        for i in range(r - p + 20, r + 20, 20):
            time.sleep(1.001)
            with ThreadPoolExecutor() as executor:
                ltc = list(range(i - 20, i))
                results = executor.map(getLtpE, ltc)
                ck = ctr-20
                for result in results:
                    ds[ck] = result
                    ck = ck + 1

            ctr = ctr + 20
        dtc.range(f"g{r-100+2}:g{r+2}").options(pd.Series, index=False).value = ds[:]
        ctrA = ctrA + 1
        # print(f"{ctrA} execution time is {time.time() - startTime}")


# getAccessTokenWithThread(200)

