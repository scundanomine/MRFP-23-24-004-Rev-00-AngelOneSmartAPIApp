from AngelOneSmartAPIApp.HistoricDataForPastAndFutureCandles import getHistoricDataForPastAndFutureCandles
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from commonudm.GetSymbolAndToken import *
from AngelOneSmartAPIApp.test import *
from ohlcdata.GetterFDS import getterFDS
from ohlcdata.GetterPDS import getterPDS
from ohlcdata.ProcessPastAndFutureCandlesData import processPastAndFutureCandlesData
from ohlcdata.SetterFDS import setterFDS
from ohlcdata.SetterPDS import setterPDS
from concurrent.futures import ThreadPoolExecutor


def getTestCandlestickData(r=300, lock=""):
    startTime = time.time()
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

    def getCandleDataC(uid):
        b = dfc["token"][uid]
        flagZero = False
        if uid < i - 3:
            try:
                data, rfDate = getHistoricDataForPastAndFutureCandles(objOneX, c, str(b))
            except:
                time.sleep(1)
                try:
                    data, rfDate = getHistoricDataForPastAndFutureCandles(objOneX, c, str(b))
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
                    rfDate = datetime.datetime.now() - c
                    flagZero = True
        else:
            try:
                data, rfDate = getHistoricDataForPastAndFutureCandles(objTwoX, c, str(b))
            except:
                time.sleep(1)
                try:
                    data, rfDate = getHistoricDataForPastAndFutureCandles(objTwoX, c, str(b))
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
                    rfDate = datetime.datetime.now() - c
                    flagZero = True
        tDf = processPastAndFutureCandlesData(rfDate, flagZero, data)
        return tDf

    # main loop for thread
    ctrA = 0
    # while 300 - (time.time() - startTime) > 0:
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        c = getterTimeDelta()
        pds = getterPDS()
        fds = getterFDS()
        ctr = 6
        for i in range(6, r + 6, 6):
            stt = time.time()
            with ThreadPoolExecutor() as executor:
                ltc = list(range(i - 6, i))
                results = executor.map(getCandleDataC, ltc)
                ck = ctr - 6
                for result in results:
                    pds.iloc[ck] = result.iloc[0]
                    fds.iloc[ck] = result.iloc[1]
                    ck = ck + 1
            ctr = ctr + 6
            timeDiff = 1 - (time.time() - stt)
            if timeDiff > 0:
                time.sleep(timeDiff)
            setterFDS(fds)
            setterPDS(pds)
        ctrA = ctrA + 1
        print(f"{ctrA} execution time is {time.time() - startTime}")


# getTestCandlestickData(300, "")
