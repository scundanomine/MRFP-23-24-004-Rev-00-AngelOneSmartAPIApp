import pandas as pd
from concurrent.futures import ThreadPoolExecutor

cdf = pd.DataFrame()


def getAllItrRSIValue(df):
    global cdf

    # get df
    cdf = df
    r = 9

    change = cdf["C"][r] - cdf["C"][r - 1]
    if change >= 0:
        cdf.loc[r, "um"] = change
        cdf.loc[r, "dm"] = 0
    else:
        cdf.loc[r, "um"] = 0
        cdf.loc[r, "dm"] = abs(change)

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

    # return round(rsi, 2)
    return rsi

# print(getRSIValue())