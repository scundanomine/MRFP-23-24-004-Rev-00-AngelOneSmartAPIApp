def getAllItrVolumeCandleSize(df):
    # get ATR
    atrVL = df["atrV"][9]
    r = 9
    
    if df["V"][r] <= 0.125 * atrVL:
        df.loc[r, "vs"] = "zero"
    elif df["V"][r] <= 0.5 * atrVL:
        df.loc[r, "vs"] = "S"
    elif df["V"][r] <= atrVL:
        df.loc[r, "vs"] = "M"
    elif df["V"][r] <= 2 * atrVL:
        df.loc[r, "vs"] = "L"
    elif df["V"][r] <= 3 * atrVL:
        df.loc[r, "vs"] = "XL"
    elif df["V"][r] <= 4 * atrVL:
        df.loc[r, "vs"] = "2XL"
    elif df["V"][r] <= 5 * atrVL:
        df.loc[r, "vs"] = "3XL"
    else:
        df.loc[r, "vs"] = "GIG"

    return df

# getVolumeCandleSize()
