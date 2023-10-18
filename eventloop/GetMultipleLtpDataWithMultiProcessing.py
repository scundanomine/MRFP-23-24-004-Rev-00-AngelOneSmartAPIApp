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
dtc = []
ctr = 20


def getAccessTokenWithThread(r):
    startTime = time.time()
    global objOneX, objTwoX, dfm, p, i, dtc, ctr
    dfm = getSymbolAndToken()

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
        global objOneX, objTwoX, dfm, i, dtc, ctr
        a = dfm["symbol"][uid]
        b = dfm["token"][uid]
        if uid < i - 10:
            ltp = objOneX.ltpData(exchange, a, str(b))
        else:
            ltp = objTwoX.ltpData(exchange, a, str(b))
        dfm.loc[uid, "ltp"] = ltp['data']['ltp']

    # main loop for thread
    ctrA = 0
    while 300 - (time.time() - startTime) > 0:
        ctr = 20
        for i in range(r - p + 20, r + 20, 20):
            time.sleep(1.001)
            with ThreadPoolExecutor() as executor:
                ltc = list(range(i - 20, i))
                executor.map(getLtpE, ltc)
            ctr = ctr + 20
        dtc.range('g1:g500').value = dfm['ltp']
        ctrA = ctrA + 1
        print(f"{ctrA} execution time is {time.time() - startTime}")


getAccessTokenWithThread(100)

# if __name__ == "__main__":
#     # get dfm
#     # get object for angel one
#     startTime = time.time()
#     dfm = getSymbolAndToken()
#
#     # create multiple process
#     with ProcessPoolExecutor() as pExecutor:
#         lt = list(range(p, math.floor(m / p) * p + p, p))
#         print(lt)
#         pExecutor.map(getAccessTokenWithThread, lt)
#     print(dfm)
#     print(f"execution time is {time.time() - startTime}")
