import time
import pandas as pd
from commonudm.GetSymbolAndToken import *
from AngelOneSmartAPIApp.test import *
from AngelOneSmartAPIApp.HistoricDataForPastTenCandles import *
from eventloop.CreateGSTDataFile import *

dfc = pd.DataFrame()
m = 500
p = 60
i = 0
objOneX = []
objTwoX = []
exchange = "NSE"
stt = 0


def getFirstCandlestickIterationData(r, fileName, lock=""):
    startTime = time.time()
    global objOneX, objTwoX, dfc, p, i, stt
    dfc = getSymbolAndToken()

    # creating session one
    while True:
        try:
            print("getting obj1")
            objOneX, accessTokenOneX = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    # creating session two
    while True:
        try:
            print("getting obj2")
            objTwoX, accessTokenOneX = getAccessTokenOne("F5SzrULj", "S53761277", "8813", "2NF7QBQP7R3NEDXC4VN6UNWYWM")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    def getCandleFirstDataC(uid):
        global objOneX, objTwoX, dfc, i
        b = dfc["token"][uid]
        b = dfc["symbol"][uid]
        if uid < i - 3:
            try:
                data = getHistoricDataForPastTenCandles(objOneX, "2023-10-20", str(b))[0]
            except:
                time.sleep(1)
                try:
                    data = getHistoricDataForPastTenCandles(objOneX, "2023-10-20", str(b))[0]
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
        else:
            try:
                data = getHistoricDataForPastTenCandles(objTwoX, "2023-10-20", str(b))[0]
            except:
                time.sleep(1)
                try:
                    data = getHistoricDataForPastTenCandles(objTwoX, "2023-10-20", str(b))[0]
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
        createGSTDataFile(uid+1, b, data)

    # main loop for thread
    for i in range(6, r + 6, 6):
        stt = time.time()
        with ThreadPoolExecutor() as executor:
            ltc = list(range(i - 6, i))
            executor.map(getCandleFirstDataC, ltc)
        timeDiff = 1 - (time.time() - stt)
        if timeDiff > 0:
            time.sleep(timeDiff)

        print(f"The execution time is {time.time() - startTime}")


getFirstCandlestickIterationData(300, "")
