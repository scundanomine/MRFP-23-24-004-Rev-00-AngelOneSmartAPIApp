def getRSIValueWithoutThreading(cdf):
    # adding new column to df
    cdf.insert(19, "umAvg", 0)
    cdf.insert(20, "dmAvg", 0)
    cdf["rsi"] = 50
    for r in range(10):
        if r == 0:
            change = cdf["C"][r] - cdf["O"][r]
        elif cdf["C"][r - 1] == 0:
            change = cdf["C"][r] - cdf["O"][r]
        else:
            change = cdf["C"][r] - cdf["C"][r - 1]
        if change >= 0:
            cdf.loc[r, "um"] = change
            cdf.loc[r, "dm"] = 0
        else:
            cdf.loc[r, "um"] = 0
            cdf.loc[r, "dm"] = abs(change)
        for k in range(r + 1):
            cdf.loc[r, "umAvg"] = cdf.loc[r, "umAvg"] + cdf.loc[k, "um"]
            cdf.loc[r, "dmAvg"] = cdf.loc[r, "dmAvg"] + cdf.loc[k, "dm"]
        cdf.loc[r, "umAvg"] = cdf.loc[r, "umAvg"] / (r + 1)
        cdf.loc[r, "dmAvg"] = cdf.loc[r, "dmAvg"] / (r + 1)
        if cdf.loc[r, "umAvg"] == 0 and cdf.loc[r, "dmAvg"] == 0:
            rsi = 50
        else:
            rsi = (cdf.loc[r, "umAvg"] / (cdf.loc[r, "umAvg"] + cdf.loc[r, "dmAvg"])) * 100
        cdf.loc[r, 'rsi'] = rsi
    # deletion of new columns
    cdf = cdf.drop(columns=["umAvg", "dmAvg"], axis=1)
    return cdf

# print(getRSIValueWithoutThreading())
