from commonudm.GetSymbolAndToken import getSymbolAndToken
from commonudm.GetterTimeDelta import getterTimeDelta
from AngelOneSmartAPIApp.test import *
from AngelOneSmartAPIApp.HistoricDataForPastTenCandles import *
from eventloop.CreateGSTDataFile import *
from concurrent.futures import ThreadPoolExecutor
import datetime

from ohlcdata.ProcessPastTenCandlesData import processPastTenCandlesData


def getTestFirstItrCandlestickData(r, isLive=False):
    print("Process for past 10 candles data started")
    startTime = time.time()
    dfc = getSymbolAndToken()
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    c = getterTimeDelta()
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
        b = dfc["token"][uid]
        flagZero = False
        if uid < i - 3:
            try:
                data, rfTime = getHistoricDataForPastTenCandles(objOneX, c, str(b))
            except:
                time.sleep(1)
                try:
                    data, rfTime = getHistoricDataForPastTenCandles(objOneX, c, str(b))
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
                    refDate = datetime.datetime.now() - c
                    rfTime = refDate - datetime.timedelta(minutes=9)
                    flagZero = True
        else:
            try:
                data, rfTime = getHistoricDataForPastTenCandles(objTwoX, c, str(b))
            except:
                time.sleep(1)
                try:
                    data, rfTime = getHistoricDataForPastTenCandles(objTwoX, c, str(b))
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
                    refDate = datetime.datetime.now() - c
                    rfTime = refDate - datetime.timedelta(minutes=9)
                    flagZero = True
        dfT = pd.DataFrame(data)
        processPastTenCandlesData(uid + 1, rfTime, dfT, flagZero)
        # getFirstItrCandlesticksProperties(uid+1, a)

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


# c = getRefDateConstant("30 Oct 2023  09:35:00.000")
# getTestFirstItrCandlestickData(60)
