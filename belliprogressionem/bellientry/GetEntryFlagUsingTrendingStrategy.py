from ltpdistribution.GetPartlyCandleLengthFromDistribution import getPartlyCandleLengthAndGenderFromDistribution
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getEntryFlagUsingTrendingStrategy(cv):
    try:
        df = getterMarketStructureDf()
        mTyp = df.loc[9, 'mTyp']
        st = df.loc[9, 'st']
        trT = df.loc[9, 'trT']
        atr = df.loc[9, "atr"]
        pl, pcg = getPartlyCandleLengthAndGenderFromDistribution(120, cv)
        if mTyp == "Bullish" and st >= 1 and trT < 5 and pcg == 'green' and pl > 0.125 * atr:
            ebf = 'F'
            esf = 'T'
        elif mTyp == "Bearish" and st <= -1 and trT < 5 and pcg == 'red' and pl > 0.125 * atr:
            ebf = 'T'
            esf = 'F'
        else:
            ebf = 'T'
            esf = 'T'
        return ebf, esf
    except Exception as e:
        print(f"Exception while getEntryFlagUsingTrendingStrategy is {e}")
        getEntryFlagUsingTrendingStrategy(cv)
