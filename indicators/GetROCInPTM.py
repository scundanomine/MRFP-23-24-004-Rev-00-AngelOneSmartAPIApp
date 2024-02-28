def getROCInPTM(df):

    # get Roc value
    try:
        roc = 0
        if df.loc[9, 'C'] != 0:
            for i in range(10):
                if df.loc[i, "C"] != 0:
                    roc = (df.loc[9, 'C'] - df.loc[i, "C"]) / df.loc[9, 'C'] * 10000
                    break
    except Exception as e:
        print(f"the exception while calculating roc is {e}")
        roc = 0
    return roc


# print(getROCInPTM())
