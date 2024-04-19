from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getExitFlagUsingBasicStrategy():
    try:
        df = getterMarketStructureDf()
        mTyp = df.loc[9, 'mTyp']
        pMTyp = df.loc[8, 'mTyp']
        # st = df.loc[9, 'st']
        trT = df.loc[9, 'trT']
        g = df.loc[9, "g"]

        # elif mTyp == "SideWise" and trT >= 3:
        #     xBF = 'F'
        #     xSF = 'F'
        if mTyp == "Bullish" and trT < 5 and g == 'red':  # condition for emergency buy exit
            xBF = 'T'
            xSF = 'T'
        elif mTyp == "Bearish" and trT < 5 and g == 'green':    # condition for emergency sell exit
            xBF = 'T'
            xSF = 'T'
        elif pMTyp == "Bullish" and pMTyp != mTyp:  # condition for emergency buy exit due to market change
            xBF = 'T'
            xSF = 'F'
        elif pMTyp == "Bearish" and pMTyp != mTyp:    # condition for emergency sell exit due to market change
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
        print(f"Exception while getExitFlagUsingBasicStrategy is {e}")
        getExitFlagUsingBasicStrategy()