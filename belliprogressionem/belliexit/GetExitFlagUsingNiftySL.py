from belliprogressionem.GetterNiftySLDf import getterNiftySLDf
from ltpdistribution.GetLTPFromDistribution import getLTPFromDistribution
from positionportfolioandmargindisplay.SetETLiveAndEntryBannedParameters import setETLiveAndEntryBannedParameters

from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket


def getExitFlagUsingNiftySL(cv, liveFlag=False):
    # startTime = time.time()
    try:
        if liveFlag:
            ltp = getterSpecificTokenLivePartlyCandleDataFromWebSocket(99926000).loc[0, '4']
        else:
            ltp = getLTPFromDistribution(120, cv)
        # pl, pcg = getPartlyCandleLengthAndGenderFromDistribution(120, cv)
        df = getterNiftySLDf()
        buySL = df.loc[0, "BuySL"]
        sellSL = df.loc[0, "SellSL"]
        if buySL != 0 and ltp <= buySL:  # condition for emergency buy exit
            xBF = 'T'
            xSF = 'F'
            setETLiveAndEntryBannedParameters("T", "T", "T", "T", 'All', 'All', "Exit due to sl hit!")
        elif sellSL != 0 and ltp >= sellSL:  # condition for emergency sell exit
            xBF = 'F'
            xSF = 'T'
            setETLiveAndEntryBannedParameters("T", "T", "T", "T", 'All', 'All', "Exit due to sl hit!")
        else:
            xBF = 'F'
            xSF = 'F'
        # print(time.time()-startTime)
        return xBF, xSF
    except Exception as e:
        print(f"Exception while getExitFlagUsingNiftySL is {e}")
        getExitFlagUsingNiftySL(cv, liveFlag)

# print(getExitFlagUsingTrendingStrategy(pd.to_timedelta(0), 0, True))
