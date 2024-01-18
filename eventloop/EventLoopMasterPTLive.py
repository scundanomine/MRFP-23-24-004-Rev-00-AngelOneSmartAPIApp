import multiprocessing
import time
from AIlists.GetAIListWithoutUdf import getAIListWithoutUdf
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterStockQtn import getterStockQtn
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
from entry.GetEntryList import getEntryList
from entrytriggeredlist.GetEntryTriggeredList import getEntryTriggeredList
from entrytriggeredlist.GetterPreBlackListForET import getterPreBlackListForET
from eventloop.CleaningAndPreRequisitePT import cleaningAndPreRequisitePT
from eventloop.EventLoopForAllITRCandlestickProperties import eventLoopForAllITRCandlestickProperties
from eventloop.EventLoopForFirstITRCandlestickProperties import eventLoopForFirstITRCandlestickProperties
from exit.TakeExit import takeExit
from ohlcdata.GetTestFirstItrCandlestickData import getTestFirstItrCandlestickData
from position.GetPosition import getPosition
from positionportfolioandmargindisplay.GetPositionPortfolioAndMarginDisplay import getPositionPortfolioAndMarginDisplay
from smartwebsocketdata.SmartApiWebSocketOne import smartApiWebSocketOne
from smartwebsocketdata.SmartApiWebSocketTwo import smartApiWebSocketTwo
from traditionalpivotalarm.CheckTraditionalPivotAlarmsWithoutThreading import \
    checkTraditionalPivotAlarmsWithoutThreading
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData
from universallist.GetUniversalListWithoutThreading import getUniversalListWithoutThreading


def candlesDataAllITREventOneOne(lock):
    print("Multiprocess One of One has been started")
    smartApiWebSocketOne()


def candlesDataAllITREventOneTwo(lock):
    print("Multiprocess One of Two has been started")
    smartApiWebSocketTwo()


def candlesPropertiesAllITREvent(lock):
    print("Multiprocess two has been started")
    eventLoopForAllITRCandlestickProperties(lock, True)
    # getAccessTokenWithThread(200, "ltpTwo.csv", lock)


def pivotAlarmEvent(lock):
    print("Multiprocess three has been started")
    # setterSRData()
    setterPrePivotData()
    checkTraditionalPivotAlarmsWithoutThreading(lock, True)


def universalListEvent(lock):
    print("Multiprocess four has been started")
    # setterDfThree()
    # setterNiftyDetailedListWithPivot()
    getUniversalListWithoutThreading(lock)


def aIListEvent(lock):
    print("Multiprocess five has been started")
    getAIListWithoutUdf(lock)


def eTListEvent(lock):
    print("Multiprocess six has been started")
    getEntryTriggeredList(lock)


def eLListEvent(lock):
    print("Multiprocess seven has been started")
    getEntryList(lock, True)


def positionListEvent(lock):
    print("Multiprocess eight has been started")
    getPosition(lock, True)


def exitEvent(lock):
    print("Multiprocess nine has been started")
    takeExit(lock, True)


def PPMEvent(lock):
    print("Multiprocess ten has been started")
    getPositionPortfolioAndMarginDisplay(lock)


def rREvent(lock):
    print("Multiprocess eleven has been started")
    getAIListWithoutUdf(lock)


# def eventLoop():
# four multiple process
if __name__ == "__main__":
    startTimeEventLoop = time.time()
    print("Running live for first time")

    # cleaning and setting prerequisite data
    cleaningAndPreRequisitePT(True)

    # getter and setter Pre data
    m = getterStockQtn()
    getterPreReferenceTime()

    # setter reference time for trading
    setterReferenceDateConstant()

    # getting past 10 candles data
    getTestFirstItrCandlestickData(m)

    # getting past 10 candles properties
    eventLoopForFirstITRCandlestickProperties()

    # setterInitialPdsAndFds()

    # setter prerequisite black list for et
    getterPreBlackListForET()

    lockA = multiprocessing.Lock()

    # starting first part 1 process of getting current and future candle data
    pOneOne = multiprocessing.Process(target=candlesDataAllITREventOneOne, args=[lockA])

    # starting first part 2 process of getting current and future candle data
    pOneTwo = multiprocessing.Process(target=candlesDataAllITREventOneTwo, args=[lockA])

    # starting second process of getting present candles data property
    pTwo = multiprocessing.Process(target=candlesPropertiesAllITREvent, args=[lockA])

    # starting Third process of getting pivot alarm
    pThree = multiprocessing.Process(target=pivotAlarmEvent, args=[lockA])

    # starting Fourth process of getting Universal list
    pFour = multiprocessing.Process(target=universalListEvent, args=[lockA])

    # starting Fifth process of getting AI list
    pFive = multiprocessing.Process(target=aIListEvent, args=[lockA])

    # starting sixth process of getting Entry triggered list
    pSix = multiprocessing.Process(target=eTListEvent, args=[lockA])

    # starting seventh process of getting entry list
    pSeven = multiprocessing.Process(target=eLListEvent, args=[lockA])

    # starting eighth process of getting position
    pEight = multiprocessing.Process(target=positionListEvent, args=[lockA])

    # starting ninth process of getting Exit
    pNine = multiprocessing.Process(target=exitEvent, args=[lockA])

    # starting tenth process of getting RR
    pTen = multiprocessing.Process(target=PPMEvent, args=[lockA])

    pOneOne.start()
    pOneTwo.start()
    pTwo.start()
    # pThree.start()
    # pFour.start()
    # pFive.start()
    # pSix.start()
    # pSeven.start()
    # pEight.start()
    # pNine.start()
    # pTen.start()

    pOneOne.join()
    pOneTwo.join()
    pTwo.join()
    # pThree.join()
    # pFour.join()
    # pFive.join()
    # pSix.join()
    # pSeven.join()
    # pEight.join()
    # pNine.join()
    # pTen.join()

    print("Multiprocess have been finished")
    print(f"execution time is {time.time() - startTimeEventLoop}")

# eventLoop()
