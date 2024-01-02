def calculationOfATRWithoutThreading(df):
    sm = 0

    for r, row in df.iterrows():
        if r == 0:
            tr = row["H"] - row["L"]
        else:
            a = row["H"] - row["L"]
            if df.loc[r - 1, "C"] == 0:
                b = 0
                c = 0
            else:
                b = abs(row["H"] - df.loc[r - 1, "C"])
                c = abs(row["L"] - df.loc[r - 1, "C"])
            lst = [a, b, c]
            tr = max(lst)
        sm = sm + tr

    # calculation for atr
    atr = sm / 10

    if df.loc[9, 'C'] != 0:
        atrPercentile = atr * 100 / df.loc[9, 'C']
    else:
        atrPercentile = 0

    return atr, atrPercentile

# calculationOfATRWithoutThreading()
