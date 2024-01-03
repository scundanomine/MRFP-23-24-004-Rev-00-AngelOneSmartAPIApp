def getAllItrVolumeCandleSize(df):
    # get ATR
    r = 9
    atrVL = df.loc[r, "atrV"]
    v = df.loc[r, "V"]
    
    if v <= 0.125 * atrVL:
        df.loc[r, "vs"] = 0
    elif v <= 0.25 * atrVL:
        df.loc[r, "vs"] = 0.25
    elif v <= 0.5 * atrVL:
        df.loc[r, "vs"] = 0.5
    elif v <= 0.75 * atrVL:
        df.loc[r, "vs"] = 0.75
    elif v <= 1 * atrVL:
        df.loc[r, "vs"] = 1
    elif v <= 1.5 * atrVL:
        df.loc[r, "vs"] = 1.5
    elif v <= 2 * atrVL:
        df.loc[r, "vs"] = 2
    elif v <= 3 * atrVL:
        df.loc[r, "vs"] = 3
    elif v <= 4 * atrVL:
        df.loc[r, "vs"] = 4
    else:
        df.loc[r, "vs"] = 5

    return df

# getVolumeCandleSize()
