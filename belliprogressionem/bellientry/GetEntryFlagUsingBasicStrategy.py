from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getEntryFlagUsingBasicStrategy():
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
        elif mTyp == "SideWise" and trT >= 3:
            ebf = 'F'
            esf = 'F'
        else:
            ebf = 'T'
            esf = 'T'
        return ebf, esf
    except Exception as e:
        print(f"Exception while getEntryFlagUsingBasicStrategy is {e}")
        getEntryFlagUsingBasicStrategy()
