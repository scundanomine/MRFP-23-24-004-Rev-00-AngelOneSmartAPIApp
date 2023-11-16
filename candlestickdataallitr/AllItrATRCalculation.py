def calculationAllItrForATR(sdf):
    # get previous Atr
    prvAtr = sdf['atr'][8]
    r = 9

    # ger last tr
    a = sdf["H"][r] - sdf["L"][r]
    b = abs(sdf["H"][r] - sdf["C"][r - 1])
    c = abs(sdf["L"][r] - sdf["C"][r - 1])
    lst = [a, b, c]
    tr = max(lst)

    # atr calculation
    atr = (prvAtr * 9 + tr) / 10
    # atrPer = atr * 100 / sdf["C"][9]
    # calculation for atr percentile
    maxPrice = sdf["C"].max()
    if maxPrice != 0:
        atrPer = atr * 100 / maxPrice
    else:
        atrPer = 0

    return atr, atrPer

# print(calculationForATR())
