from GetCandlestickDf import *


def getROCInPTM():
    # get data
    df = getCandlestickDf()

    # get Roc value
    roc = (df["C"][9] - df["C"][0]) / df["C"][0] * 10000
    roc = round(roc, 2)
    return roc


print(getROCInPTM())
