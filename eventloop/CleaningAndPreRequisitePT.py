import time

from AIlists.CleaningAndSettingAIList import cleaningAndSettingAIList
from candlestickdata.CleaningAndSettingGSTDataFiles import cleaningAndSettingGSTDataFiles
from commonudm.GetterPreExitTime import getterPreExitTime
from commonudm.GetterPreStockQtn import getterPreStockQtn
from commonudm.SetterNiftyDetailedListWithPivots import setterNiftyDetailedListWithPivot
from commonudm.SetterRequiredSymbolAndTokenList import setterRequiredSymbolAndTokenList
from entry.SetterPreECBList import setterPreECBList
from entry.SetterPreEntryList import setterPreEntryList
from entrytriggeredlist.CleaningAndSettingETList import cleaningAndSettingETList
from entrytriggeredlist.GetterPreBlackListForET import getterPreBlackListForET
from exit.SetterPreExitInputs import setterPreExitInputs
from margin.GetterPreMargin import getterPreMargin
from ohlcdata.CleaningAndSettingPastTenCandleData import cleaningAndSettingPastTenCandleData
from ohlcdata.SetterInitialPdsAndFds import setterInitialPdsAndFds
from portfolio.GetterPreFixedPortfolio import getterPreFixedPortfolio
from position.GetterPrePositionId import getterPrePositionId
from position.SetterPrePositionList import setterPrePositionList
from readandrecord.SetterPrePECBListRR import setterPrePECBListRR
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData
from traditionalpivotalarm.SetterSRData import setterSRData
from universallist.CleaningAndSettingUniversalList import cleaningAndSettingUniversalList
from universallist.SetterDfThree import setterDfThree


def cleaningAndPreRequisitePT(isLive=False):
    # startTime = time.time()
    # getter and setter Pre data
    getterPreStockQtn()

    # getter pre exit time
    getterPreExitTime()

    # setter required symbol and token list
    setterRequiredSymbolAndTokenList()

    # cleaning and setting data for past 10 candles data
    cleaningAndSettingPastTenCandleData()

    # cleaning and setting GST data files
    cleaningAndSettingGSTDataFiles()

    # cleaning and setting past pds and fds and fFds
    if not isLive:
        setterInitialPdsAndFds()

    # setter pre pivot data
    setterSRData()
    setterPrePivotData()

    # cleaning and setting universal list data
    setterDfThree()
    setterNiftyDetailedListWithPivot()
    cleaningAndSettingUniversalList()

    # cleaning and setting AI list
    cleaningAndSettingAIList()

    # cleaning the setting the Entry Triggered list
    getterPreBlackListForET()
    cleaningAndSettingETList()

    # cleaning the setting the Entry list
    setterPreECBList()
    setterPreEntryList()

    # cleaning the setting the position list
    setterPrePositionList()
    getterPrePositionId()

    # setter pre exit inputs
    setterPreExitInputs()

    # cleaning the setting the portfolio and margin
    getterPreFixedPortfolio()
    getterPreMargin()

    # cleaning for RR
    setterPrePECBListRR()
    # print(f"execution time for cleaning is {time.time() - startTime}")


# cleaningAndPreRequisitePT()
