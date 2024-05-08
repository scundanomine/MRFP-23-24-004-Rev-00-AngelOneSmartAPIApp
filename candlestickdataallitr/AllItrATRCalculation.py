def calculationAllItrForATR(sdf):
    # get previous Atr
    prvAtr = sdf['atr'][8]
    r = 9

    if sdf.loc[r, 'C'] != 0:
        if sdf.loc[r - 1, 'C'] != 0:
            # ger last tr
            a = sdf["H"][r] - sdf["L"][r]
            b = abs(sdf["H"][r] - sdf["C"][r - 1])
            c = abs(sdf["L"][r] - sdf["C"][r - 1])
            lst = [a, b, c]
            tr = max(lst)
        else:
            tr = sdf["H"][r] - sdf["L"][r]

        # atr calculation with EMA
        # atr = (prvAtr * 9 + tr) / 10
        atr = (tr - prvAtr) * 2 / 11 + prvAtr
        # atrPer = atr * 100 / sdf["C"][9]
        # calculation for atr percentile
        maxPrice = sdf.loc[9, "C"]
        if maxPrice != 0:
            atrPer = atr * 100 / maxPrice
        else:
            atrPer = 0
    else:
        atr = prvAtr
        atrPer = sdf.loc[8, 'atrPer']

    return atr, atrPer

# print(calculationForATR())
