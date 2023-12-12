import multiprocessing
from commonudm.GetterPreExitTime import getterPreExitTime
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterPreStockQtn import getterPreStockQtn
from commonudm.GetterPreTimeDelta import getterPreTimeDelta
from commonudm.GetterStockQtn import getterStockQtn
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
from commonudm.SetterRequiredSymbolAndTokenList import setterRequiredSymbolAndTokenList
from eventloop.EventLoopForAllITRCandlestickProperties import eventLoopForAllITRCandlestickProperties
from eventloop.EventLoopForFirstITRCandlestickProperties import eventLoopForFirstITRCandlestickProperties
from ohlcdata.GetTestCandlestickData import getTestCandlestickData
from ohlcdata.GetTestFirstItrCandlestickData import getTestFirstItrCandlestickData
import time
from ohlcdata.SetterInitialPdsAndFds import setterInitialPdsAndFds
from traditionalpivotalarm.CheckTraditionalPivotAlarmsWithoutThreading import checkTraditionalPivotAlarmsWithoutThreading
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData
from traditionalpivotalarm.SetterSRData import setterSRData


# function for PivotAlarm
def candlesDataAllITREvent(n, lock):
    print("Multiprocess One has been started")
    getTestCandlestickData(n, lock)


def candlesPropertiesAllITREvent(lock):
    print("Multiprocess two has been started")
    eventLoopForAllITRCandlestickProperties(lock)
    # getAccessTokenWithThread(200, "ltpTwo.csv", lock)


def pivotAlarmEvent(lock):
    print("Multiprocess three has been started")
    setterSRData()
    setterPrePivotData()
    checkTraditionalPivotAlarmsWithoutThreading(lock)
    # getLtpFromThread(objE)
    # getAccessTokenWithThread(300, "ltpThree.csv", lock)


def readRecordEventFour(lock):
    print("Multiprocess four has been started")
    # getLtpFromThread(objE)
    # getAccessTokenWithThread(400, "ltpFour.csv", lock)


def readRecordEventFive(lock):
    print("Multiprocess five has been started")
    # getLtpFromThread(objE)
    # getAccessTokenWithThread(500, "ltpFive.csv", lock)


def eventLoop():
    startTime = time.time()
    # four multiple process
    if __name__ == "__main__":
        # getter and setter Pre data
        getterPreStockQtn()
        n = getterStockQtn()
        getterPreExitTime()
        getterPreReferenceTime()
        # setter reference time for trading
        setterReferenceDateConstant()
        getterPreTimeDelta()

        # setter required symbol and token list
        setterRequiredSymbolAndTokenList()

        # getting past 10 candles data
        getTestFirstItrCandlestickData(n)

        # getting past 10 candles properties
        eventLoopForFirstITRCandlestickProperties()

        setterInitialPdsAndFds()

        lock = multiprocessing.Lock()

        # starting first process of getting current and future candle data
        pOne = multiprocessing.Process(target=candlesDataAllITREvent, args=[n, lock])

        # starting second process of getting present candles data property
        pTwo = multiprocessing.Process(target=candlesPropertiesAllITREvent, args=[lock])

        # starting Third process of getting pivot alarm
        pThree = multiprocessing.Process(target=pivotAlarmEvent, args=[lock])

        pOne.start()
        pTwo.start()
        pThree.start()

        pOne.join()
        pTwo.join()
        pThree.join()

        print("Multiprocess have been finished")
        print(f"execution time is {time.time() - startTime}")


eventLoop()
