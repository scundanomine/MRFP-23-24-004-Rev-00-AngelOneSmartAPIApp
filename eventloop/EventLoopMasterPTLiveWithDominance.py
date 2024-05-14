import multiprocessing
import time

from AIlists.GetAIListWithoutUdf import getAIListWithoutUdf
from belliprogressionem.GetAllItrStrategyEntryAndExitFlags import getAllItrStrategyEntryAndExitFlags
from commonudm.GetterFirstTimeRunFlagFromExcel import getterFirstTimeRunFlagFromExcel
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterStockQtn import getterStockQtn
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
from commonudm.SetterReportDateForRR import setterReportDateForRR
from entry.GetEntryList import getEntryList
from entry.GetEntryListWithDominance import getEntryListWithDominance
from entrytriggeredlist.GetEntryTriggeredList import getEntryTriggeredList
from entrytriggeredlist.GetterPreBlackListForET import getterPreBlackListForET
from eventloop.CleaningAndPreRequisitePT import cleaningAndPreRequisitePT
from eventloop.EventLoopForAllITRCandlestickProperties import eventLoopForAllITRCandlestickProperties
from eventloop.EventLoopForFirstITRCandlestickProperties import eventLoopForFirstITRCandlestickProperties
from exit.TakeExit import takeExit
from exit.TakeExitWithDominance import takeExitWithDominance
from marketstructure.GetAllItrMarketStructure import getAllItrMarketStructure
from marketstructure.GetFirstItrMarketStructure import getFirstItrMarketStructure
from ohlcdata.GetTestFirstItrCandlestickData import getTestFirstItrCandlestickData
from pastthirtycandles.GetPastThirtyCandles import getPastThirtyCandles
from pastthirtycandles.GetPrePastThirtyCandle import getPrePastThirtyCandle
from position.GetPosition import getPosition
from position.GetPositionWithDominance import getPositionWithDominance
from positionportfolioandmargindisplay.GetPositionPortfolioAndMarginDisplay import getPositionPortfolioAndMarginDisplay
from readandrecord.CleaningAllRecordsFromRR import cleaningAllRecordsFromRR
from readandrecord.CreateRRDirectoriesIfNotExist import createRRDirectoriesIfNotExist
from readandrecord.GetRecords import getRecords
from universallist.GetUniversalListWithoutThreading import getUniversalListWithoutThreading


def candlesPropertiesAllITREvent():
    print("Multiprocess One has been started")
    eventLoopForAllITRCandlestickProperties(True)


def universalListEvent():
    print("Multiprocess Two has been started")
    # setterDfThree()
    # setterNiftyDetailedListWithPivot()
    getUniversalListWithoutThreading(True)


def aIListEvent():
    print("Multiprocess three has been started")
    getAIListWithoutUdf(True)


def eTListEvent(lock):
    print("Multiprocess four has been started")
    getEntryTriggeredList(lock, True)


def eLListEvent(lock):
    print("Multiprocess five has been started")
    getEntryListWithDominance(lock, True)


def positionListEvent(lock):
    print("Multiprocess six has been started")
    getPositionWithDominance(lock, True)


def exitEvent(lock):
    print("Multiprocess seven has been started")
    takeExitWithDominance(lock, True)


def PPMEvent():
    print("Multiprocess eight has been started")
    getPositionPortfolioAndMarginDisplay(True)


def rREvent():
    print("Multiprocess nine has been started")
    getRecords()


def rPastThirtyCandles():
    print("Multiprocess ten has been started")
    getPastThirtyCandles(True)


def marketStructureData():
    print("Multiprocess eleven has been started")
    getAllItrMarketStructure(True)


def rEntryAndExitStrategyFlags():
    print("Multiprocess twelve has been started")
    getAllItrStrategyEntryAndExitFlags(True)


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

    # setPrePastTimeByMin(True)   # check the validity of it
    # setPrePastTimeByMinEntryBanned(True)  # check the validity of it

    # setter report date and required data for rr
    setterReportDateForRR()
    createRRDirectoriesIfNotExist()
    flagF = getterFirstTimeRunFlagFromExcel()
    if flagF == 'T':
        cleaningAllRecordsFromRR()  # need to optimize it

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

    # starting one process of getting present candles data property
    pOne = multiprocessing.Process(target=candlesPropertiesAllITREvent, args=[])

    # starting two process of getting Universal list
    pTwo = multiprocessing.Process(target=universalListEvent, args=[])

    # starting three process of getting AI list
    pThree = multiprocessing.Process(target=aIListEvent, args=[])

    # starting four process of getting Entry triggered list
    pFour = multiprocessing.Process(target=eTListEvent, args=[lockA])

    # starting five process of getting entry list
    pFive = multiprocessing.Process(target=eLListEvent, args=[lockA])

    # starting six process of getting position
    pSix = multiprocessing.Process(target=positionListEvent, args=[lockA])

    # starting seven process of getting Exit
    pSeven = multiprocessing.Process(target=exitEvent, args=[lockA])

    # starting eight process of position, portfolio and margin display
    pEight = multiprocessing.Process(target=PPMEvent, args=[])

    # starting nine process of position, portfolio and margin display
    pNine = multiprocessing.Process(target=rREvent, args=[])

    # starting 10th process of position, portfolio and margin display
    pTen = multiprocessing.Process(target=rPastThirtyCandles, args=[])

    # starting 11th process of market structure data
    pEleven = multiprocessing.Process(target=marketStructureData, args=[])

    # starting 12th process of Entry and exit strategy flags
    pTwelve = multiprocessing.Process(target=rEntryAndExitStrategyFlags, args=[])

    pOne.start()
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
    # pTwelve.start()

    pOne.join()
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
    # pTwelve.join()

    print("Multiprocess have been finished")
    print(f"execution time is {time.time() - startTimeEventLoop}")

# eventLoop()
