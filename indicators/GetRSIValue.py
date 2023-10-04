from commonudm.GetCandlestickTenMinuteData import *
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

cdf = pd.DataFrame()


def getRSIValue():
    global cdf

    # get df
    df = getCandlestickTenMinuteData()
    n = len(df)

    # create custom df
    cdf = pd.DataFrame(index=list(range(n)), columns=["close", "um", "dm"])
    cdf['close'] = df['C']
    cdf['um'] = 0
    cdf['dm'] = 0

    # function for um and dm
    def getUmAndDm(r):
        global cdf
        change = cdf["close"][r] - cdf["close"][r - 1]
        if change >= 0:
            cdf.iloc[r, "um"] = change
            cdf.iloc[r, "dm"] = 0
        else:
            cdf.iloc[r, "um"] = 0
            cdf.iloc[r, "dm"] = abs(change)

    with ThreadPoolExecutor() as executor:
        lt = list(range(1, n))
        results = executor.map(getUmAndDm, lt)

    # calculate upward and downward avg
    umAvg = cdf["um"].sum() / (n - 1)
    dmAvg = cdf["dm"].sum() / (n - 1)
    relStrength = umAvg / dmAvg
    rsi = 100 - 100/(relStrength+1)
    return rsi


getRSIValue()