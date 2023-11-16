def getROCInPTM(df):
    # get data
    # df = getCandlestickDf()

    # get Roc value
    try:
        roc = (df["C"][9] - df["C"][0]) / df["C"].max() * 10000
    except Exception as e:
        print(f"the exception while calculating roc is {e}")
        roc = 0
    # roc = round(roc, 2)
    return roc


# print(getROCInPTM())
