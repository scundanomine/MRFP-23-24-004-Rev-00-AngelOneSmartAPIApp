def getAllItrSMAForNiftyIndex(cdf):
    ctr = 0
    sumA = 0

    # ATR for volume
    for index, row in cdf.iterrows():
        if row["C"] != 0:
            sumA = sumA + row["C"]
            ctr = ctr + 1

    if ctr != 0:
        sma = sumA / ctr
    else:
        sma = 0

    return sma

# getATRForVolume()
