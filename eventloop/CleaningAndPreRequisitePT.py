from AIlists.CleaningAndSettingAIList import cleaningAndSettingAIList
from belliprogressionem.SetterPreETStrategyFlag import setterPreETStrategyFlag
from belliprogressionem.SetterPreExitStrategyFlag import setterPreExitStrategyFlag
from candlestickdata.CleaningAndSettingGSTDataFiles import cleaningAndSettingGSTDataFiles
from commonudm.GetterPreExitTime import getterPreExitTime
from commonudm.GetterPreStockQtn import getterPreStockQtn
from commonudm.SetterNiftyDetailedListWithPivots import setterNiftyDetailedListWithPivot
from commonudm.SetterRequiredSymbolAndTokenList import setterRequiredSymbolAndTokenList
from belliprogressionem.GetterETStrategyFlag import getterETStrategyFlag
from entry.SetterPreECBList import setterPreECBList
from entry.SetterPreEntryList import setterPreEntryList
from entrytriggeredlist.CleaningAndSettingETList import cleaningAndSettingETList
from entrytriggeredlist.GetterPreBlackListForET import getterPreBlackListForET
from exit.SetterPreExitInputs import setterPreExitInputs
from margin.GetterPreMargin import getterPreMargin
from ohlcdata.CleaningAndSettingPastTenCandleData import cleaningAndSettingPastTenCandleData
from ohlcdata.SetterPrePdsFdsAndFfdsList import setterPrePdsFdsAndFfdsList
from pastthirtycandles.SetterDfOneForPastThirtyCandles import setterDfOneForPastThirtyCandles
from portfolio.GetterPreFixedPortfolio import getterPreFixedPortfolio
from position.SetterPrePositionList import setterPrePositionList
from positionportfolioandmargindisplay.SetterPreEntryBanned import setterPreEntryBanned
from readandrecord.SetterPrePECBListRR import setterPrePECBListRR
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData
from traditionalpivotalarm.SetterSRData import setterSRData
from universallist.CleaningAndSettingUniversalList import cleaningAndSettingUniversalList
from universallist.SetterDfThree import setterDfThree


def cleaningAndPreRequisitePT(isLive=False, cleaningFlag=False):
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
        setterPrePdsFdsAndFfdsList()

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
    setterPreETStrategyFlag()
    setterPreExitStrategyFlag()

    # cleaning the setting the position list
    setterPrePositionList()

    # setter pre exit inputs
    setterPreExitInputs()

    # cleaning the setting the portfolio and margin
    getterPreFixedPortfolio()
    getterPreMargin()
    setterPreEntryBanned()

    # cleaning for RR
    setterPrePECBListRR()
    # print(f"execution time for cleaning is {time.time() - startTime}")

    # cleaning and setter for past thirty candles
    setterDfOneForPastThirtyCandles()

# cleaningAndPreRequisitePT()
