def getROCInPTM(df):
    # get data
    # df = getCandlestickDf()

    # get Roc value
    try:
        if df.loc[0, "C"] == 0 or df.loc[9, "C"] == 0:
            roc = 0
        else:
            roc = (df["C"][9] - df["C"][0]) / df["C"][9] * 10000
    except Exception as e:
        print(f"the exception while calculating roc is {e}")
        roc = 0
    return roc


# print(getROCInPTM())
