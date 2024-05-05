from ltpdistribution.GetPartlyCandleLengthFromDistribution import getPartlyCandleLengthAndGenderFromDistribution
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from smartwebsocketdata.GetPartlyCandleLengthAndGenderFromWebSocket import getPartlyCandleLengthAndGenderFromWebSocket


def getEntryFlagUsingTrendingStrategy(cv, liveFlag=False):
    try:
        df = getterMarketStructureDf()
        mTyp = df.loc[9, 'mTyp']
        pMTyp = df.loc[8, 'mTyp']
        st = df.loc[9, 'st']
        trT = df.loc[9, 'trT']
        atr = df.loc[9, "atr"]
        if mTyp == pMTyp:
            if liveFlag:
                pl, pcg = getPartlyCandleLengthAndGenderFromWebSocket(99926012)
            else:
                pl, pcg = getPartlyCandleLengthAndGenderFromDistribution(120, cv)
        else:
            if liveFlag:
                pl, pcg = getPartlyCandleLengthAndGenderFromWebSocket(99926012, True)
            else:
                pl, pcg = getPartlyCandleLengthAndGenderFromDistribution(120, cv, True)
        # Strategy for market change
        if mTyp == "Bullish" and st >= 1 and trT < 7 and pcg == 'green' and pl > 0.0625 * atr:
            ebf = 'F'
            esf = 'T'
        elif mTyp == "Bearish" and st <= -1 and trT < 7 and pcg == 'red' and pl > 0.0625 * atr:
            ebf = 'T'
            esf = 'F'
        else:
            ebf = 'T'
            esf = 'T'
        return ebf, esf
    except Exception as e:
        print(f"Exception while getEntryFlagUsingTrendingStrategy is {e}")
        getEntryFlagUsingTrendingStrategy(cv)
