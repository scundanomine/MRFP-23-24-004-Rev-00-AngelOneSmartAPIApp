from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getEntryFlagUsingTrendingStrategy():
    try:
        df = getterMarketStructureDf()
        mTyp = df.loc[9, 'mTyp']
        st = df.loc[9, 'st']
        trT = df.loc[9, 'trT']
        if mTyp == "Bullish" and st >= 1 and trT < 5:
            ebf = 'F'
            esf = 'T'
        elif mTyp == "Bearish" and st <= -1 and trT < 5:
            ebf = 'T'
            esf = 'F'
        else:
            ebf = 'T'
            esf = 'T'
        return ebf, esf
    except Exception as e:
        print(f"Exception while getEntryFlagUsingTrendingStrategy is {e}")
        getEntryFlagUsingTrendingStrategy()
