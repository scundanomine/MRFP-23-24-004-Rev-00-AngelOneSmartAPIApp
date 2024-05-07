import time
from ltpdistribution.GetPartlyCandleLengthFromDistribution import getPartlyCandleLengthAndGenderFromDistribution
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from positionportfolioandmargindisplay.SetETLiveAndEntryBannedParameters import setETLiveAndEntryBannedParameters
from smartwebsocketdata.GetPartlyCandleLengthAndGenderFromWebSocket import getPartlyCandleLengthAndGenderFromWebSocket


def getExitFlagUsingTrendingStrategy(cv, pSize=0, liveFlag=False):
    try:
        df = getterMarketStructureDf()
        mTyp = df.loc[9, 'mTyp']
        pMTyp = df.loc[8, 'mTyp']
        # st = df.loc[9, 'st']
        # trT = df.loc[9, 'trT']
        # g = df.loc[9, "g"]
        atr = df.loc[9, "atr"]
        if liveFlag:
            pl, pcg = getPartlyCandleLengthAndGenderFromWebSocket(99926012)
        else:
            pl, pcg = getPartlyCandleLengthAndGenderFromDistribution(120, cv)
        # pl, pcg = getPartlyCandleLengthAndGenderFromDistribution(120, cv)

        if mTyp == "Bullish" and pcg == 'red' and pl > 0.6 * atr:  # condition for emergency buy exit
            xBF = 'F'
            xSF = 'F'
            setETLiveAndEntryBannedParameters("T", "T", "F", "F", 'All', 'Default', time.time(), mTyp, pSize, "doomed!")
        elif mTyp == "Bearish" and pcg == 'green' and pl > 0.6 * atr:  # condition for emergency sell exit
            xBF = 'F'
            xSF = 'F'
            setETLiveAndEntryBannedParameters("T", "T", "F", "F", 'All', 'Default', time.time(), mTyp, pSize, "doomed!")
        elif mTyp == "Bullish" and pcg == 'red' and pl > 1.5 * atr:  # condition for emergency buy exit
            xBF = 'T'
            xSF = 'T'
            setETLiveAndEntryBannedParameters("T", "T", "T", "T", 'All', 'All', time.time(), mTyp, pSize)
        elif mTyp == "Bearish" and pcg == 'green' and pl > 1.5 * atr:  # condition for emergency sell exit
            xBF = 'T'
            xSF = 'T'
            setETLiveAndEntryBannedParameters("T", "T", "T", "T", 'All', 'All', time.time(), mTyp, pSize)
        elif pMTyp == "Bullish" and mTyp == "Bearish":  # condition for emergency buy exit due to market change
            xBF = 'T'
            xSF = 'F'
        elif pMTyp == "Bearish" and mTyp == "Bullish":  # condition for emergency sell exit due to market change
            xBF = 'F'
            xSF = 'T'
        elif mTyp == "Bullish":
            xBF = 'F'
            xSF = 'T'
        elif mTyp == "Bearish":
            xBF = 'T'
            xSF = 'F'
        else:
            xBF = 'F'
            xSF = 'F'
        return xBF, xSF
    except Exception as e:
        print(f"Exception while getExitFlagUsingTrendingStrategy is {e}")
        getExitFlagUsingTrendingStrategy(cv, pSize, liveFlag)


# print(getExitFlagUsingTrendingStrategy(pd.to_timedelta(0), 0, True))
