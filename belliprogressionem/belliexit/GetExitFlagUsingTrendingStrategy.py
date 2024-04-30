import time

from ltpdistribution.GetPartlyCandleLengthFromDistribution import getPartlyCandleLengthAndGenderFromDistribution
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from positionportfolioandmargindisplay.SetETLiveAndEntryBannedParameters import setETLiveAndEntryBannedParameters


def getExitFlagUsingTrendingStrategy(cv, pSize=0):
    try:
        df = getterMarketStructureDf()
        mTyp = df.loc[9, 'mTyp']
        pMTyp = df.loc[8, 'mTyp']
        # st = df.loc[9, 'st']
        # trT = df.loc[9, 'trT']
        # g = df.loc[9, "g"]
        atr = df.loc[9, "atr"]

        pl, pcg = getPartlyCandleLengthAndGenderFromDistribution(120, cv)

        if mTyp == "Bullish" and pcg == 'red' and pl > 0.6 * atr:  # condition for emergency buy exit
            xBF = 'T'
            xSF = 'T'
            setETLiveAndEntryBannedParameters("T", "T", 'All', 'All', time.time(), mTyp, pSize)
        elif mTyp == "Bearish" and pcg == 'green' and pl > 0.6 * atr:  # condition for emergency sell exit
            xBF = 'T'
            xSF = 'T'
            setETLiveAndEntryBannedParameters("T", "T", 'All', 'All', time.time(), mTyp, pSize)
        elif pMTyp == "Bullish" and pMTyp != mTyp:  # condition for emergency buy exit due to market change
            xBF = 'T'
            xSF = 'F'
        elif pMTyp == "Bearish" and pMTyp != mTyp:  # condition for emergency sell exit due to market change
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
        getExitFlagUsingTrendingStrategy(cv)
