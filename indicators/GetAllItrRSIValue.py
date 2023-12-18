import pandas as pd

cdf = pd.DataFrame()


def getAllItrRSIValue(df):
    global cdf

    # get df
    cdf = df
    r = 9
    if cdf["C"][r - 1] == 0:
        change = cdf["C"][r] - cdf["O"][r]
    else:
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

    # rsi = 100 - 100 / (relStrength + 1)
    if umAvg == 0 and dmAvg == 0:
        rsi = 50
    else:
        rsi = (umAvg / (umAvg + dmAvg)) * 100

    cdf.loc[9, 'rsi'] = rsi

    # return round(rsi, 2)
    return rsi

# print(getRSIValue())
