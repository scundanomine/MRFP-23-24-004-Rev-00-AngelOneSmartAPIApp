def getVolumeCandleSizeWithoutThreading(df):
    # get ATR
    atrVL = df["atrV"][9]
    for r, row in df.iterrows():
        if row["V"] <= 0.125 * atrVL:
            df.loc[r, "vs"] = 0
        elif row["V"] <= 0.25 * atrVL:
            df.loc[r, "vs"] = 0.25
        elif row["V"] <= 0.5 * atrVL:
            df.loc[r, "vs"] = 0.5
        elif row["V"] <= 0.75 * atrVL:
            df.loc[r, "vs"] = 0.75
        elif row["V"] <= 1 * atrVL:
            df.loc[r, "vs"] = 1
        elif row["V"] <= 1.5 * atrVL:
            df.loc[r, "vs"] = 1.5
        elif row["V"] <= 2 * atrVL:
            df.loc[r, "vs"] = 2
        elif row["V"] <= 3 * atrVL:
            df.loc[r, "vs"] = 3
        elif row["V"] <= 4 * atrVL:
            df.loc[r, "vs"] = 4
        else:
            df.loc[r, "vs"] = 5

    return df


# getVolumeCandleSize()
