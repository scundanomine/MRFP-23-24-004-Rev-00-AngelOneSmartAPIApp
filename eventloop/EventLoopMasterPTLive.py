import multiprocessing
import time
from AIlists.GetAIListWithoutUdf import getAIListWithoutUdf
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterStockQtn import getterStockQtn
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
from commonudm.SetterReportDateForRR import setterReportDateForRR
from entry.GetEntryList import getEntryList
from entrytriggeredlist.GetEntryTriggeredList import getEntryTriggeredList
from entrytriggeredlist.GetterPreBlackListForET import getterPreBlackListForET
from eventloop.CleaningAndPreRequisitePT import cleaningAndPreRequisitePT
from eventloop.EventLoopForAllITRCandlestickProperties import eventLoopForAllITRCandlestickProperties
from eventloop.EventLoopForFirstITRCandlestickProperties import eventLoopForFirstITRCandlestickProperties
from exit.TakeExit import takeExit
from marketstructure.GetAllItrMarketStructure import getAllItrMarketStructure
from marketstructure.GetFirstItrMarketStructure import getFirstItrMarketStructure
from ohlcdata.GetTestFirstItrCandlestickData import getTestFirstItrCandlestickData
from pastthirtycandles.GetPastThirtyCandles import getPastThirtyCandles
from pastthirtycandles.GetPrePastThirtyCandle import getPrePastThirtyCandle
from position.GetPosition import getPosition
from positionportfolioandmargindisplay.GetPositionPortfolioAndMarginDisplay import getPositionPortfolioAndMarginDisplay
from readandrecord.CleaningAllRecordsFromRR import cleaningAllRecordsFromRR
from readandrecord.CreateRRDirectoriesIfNotExist import createRRDirectoriesIfNotExist
from readandrecord.GetRecords import getRecords
from traditionalpivotalarm.CheckTraditionalPivotAlarmsWithoutThreading import \
    checkTraditionalPivotAlarmsWithoutThreading
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData
from universallist.GetUniversalListWithoutThreading import getUniversalListWithoutThreading


def candlesPropertiesAllITREvent():
    print("Multiprocess two has been started")
    eventLoopForAllITRCandlestickProperties(True)


def pivotAlarmEvent():
    print("Multiprocess three has been started")
    # setterSRData()
    setterPrePivotData()
    checkTraditionalPivotAlarmsWithoutThreading(True)


def universalListEvent():
    print("Multiprocess four has been started")
    # setterDfThree()
    # setterNiftyDetailedListWithPivot()
    getUniversalListWithoutThreading(True)


def aIListEvent():
    print("Multiprocess five has been started")
    getAIListWithoutUdf(True)


def eTListEvent(lock):
    print("Multiprocess six has been started")
    getEntryTriggeredList(lock, True)


def eLListEvent(lock):
    print("Multiprocess seven has been started")
    getEntryList(lock, True)


def positionListEvent(lock):
    print("Multiprocess eight has been started")
    getPosition(lock, True)


def exitEvent(lock):
    print("Multiprocess nine has been started")
    takeExit(lock, True)


def PPMEvent():
    print("Multiprocess ten has been started")
    getPositionPortfolioAndMarginDisplay(True)


def rREvent():
    print("Multiprocess eleven has been started")
    getRecords()


def rPastThirtyCandles():
    print("Multiprocess twelve has been started")
    getPastThirtyCandles(True)


def marketStructureData():
    print("Multiprocess thirteen has been started")
    getAllItrMarketStructure(True)


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

    # setter report date and required data for rr
    setterReportDateForRR()
    createRRDirectoriesIfNotExist()
    cleaningAllRecordsFromRR()

    # getting past 10 candles data
    getTestFirstItrCandlestickData(m, True)

    # getting past 10 candles properties
    eventLoopForFirstITRCandlestickProperties()

    # get market structure data for past nifty 100
    getFirstItrMarketStructure()

    # setter pre past 30 candles data
    getPrePastThirtyCandle()

    # setterInitialPdsAndFds()

    # setter prerequisite black list for et
    getterPreBlackListForET()

    lockA = multiprocessing.Lock()

    # starting second process of getting present candles data property
    pTwo = multiprocessing.Process(target=candlesPropertiesAllITREvent, args=[])

    # starting Third process of getting pivot alarm
    pThree = multiprocessing.Process(target=pivotAlarmEvent, args=[])

    # starting Fourth process of getting Universal list
    pFour = multiprocessing.Process(target=universalListEvent, args=[])

    # starting Fifth process of getting AI list
    pFive = multiprocessing.Process(target=aIListEvent, args=[])

    # starting sixth process of getting Entry triggered list
    pSix = multiprocessing.Process(target=eTListEvent, args=[lockA])

    # starting seventh process of getting entry list
    pSeven = multiprocessing.Process(target=eLListEvent, args=[lockA])

    # starting eighth process of getting position
    pEight = multiprocessing.Process(target=positionListEvent, args=[lockA])

    # starting ninth process of getting Exit
    pNine = multiprocessing.Process(target=exitEvent, args=[lockA])

    # starting tenth process of position, portfolio and margin display
    pTen = multiprocessing.Process(target=PPMEvent, args=[])

    # starting tenth process of position, portfolio and margin display
    pEleven = multiprocessing.Process(target=rREvent, args=[])

    # starting 12th process of position, portfolio and margin display
    pTwelve = multiprocessing.Process(target=rPastThirtyCandles, args=[])

    # starting 13th process of market structure data
    pThirteen = multiprocessing.Process(target=rPastThirtyCandles, args=[])

    pTwo.start()
    pThree.start()
    pFour.start()
    pFive.start()
    pSix.start()
    pSeven.start()
    pEight.start()
    pNine.start()
    pTen.start()
    pEleven.start()
    pTwelve.start()
    pThirteen.start()

    pTwo.join()
    pThree.join()
    pFour.join()
    pFive.join()
    pSix.join()
    pSeven.join()
    pEight.join()
    pNine.join()
    pTen.join()
    pEleven.join()
    pTwelve.join()
    pThirteen.join()

    print("Multiprocess have been finished")
    print(f"execution time is {time.time() - startTimeEventLoop}")

# eventLoop()
