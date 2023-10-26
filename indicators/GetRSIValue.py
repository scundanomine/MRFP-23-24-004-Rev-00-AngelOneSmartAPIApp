from commonudm.GetCandlestickTenMinuteData import *
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

cdf = pd.DataFrame()


def getRSIValue(df):
    global cdf
    startTime = time.time()
    # get df
    # df = getCandlestickTenMinuteData()
    # n = len(df)

    # create custom df
    cdf = pd.DataFrame(index=list(range(10)), columns=["close", "um", "dm"])
    cdf['close'] = df['C']
    cdf['um'] = 0
    cdf['dm'] = 0

    # function for um and dm
    def getUmAndDm(r):
        global cdf
        change = cdf["close"][r] - cdf["close"][r - 1]
        if change >= 0:
            cdf.loc[r, "um"] = change
            cdf.loc[r, "dm"] = 0
        else:
            cdf.loc[r, "um"] = 0
            cdf.loc[r, "dm"] = abs(change)

    with ThreadPoolExecutor() as executor:
        lt = list(range(1, 10))
        results = executor.map(getUmAndDm, lt)

    # calculate upward and downward avg
    umAvg = cdf["um"].sum() / 9
    dmAvg = cdf["dm"].sum() / 9
    try:
        if umAvg == 0 and dmAvg == 0:
            relStrength = 1
        else:
            relStrength = umAvg / dmAvg
    except:
        relStrength = 1000000

    rsi = 100 - 100 / (relStrength + 1)
    print(f"time of execution is {time.time() - startTime}")
    # return round(rsi, 2)
    return rsi

# print(getRSIValue())
