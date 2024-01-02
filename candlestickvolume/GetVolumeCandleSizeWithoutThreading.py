def getVolumeCandleSizeWithoutThreading(vdf):
    # get ATR
    atrVL = vdf["atrV"][9]
    for r, row in vdf.iterrows():
        if row["V"] <= 0.125 * atrVL:
            vdf.loc[r, "vs"] = "zero"
        elif row["V"] <= 0.5 * atrVL:
            vdf.loc[r, "vs"] = "S"
        elif row["V"] <= atrVL:
            vdf.loc[r, "vs"] = "M"
        elif row["V"] <= 2 * atrVL:
            vdf.loc[r, "vs"] = "L"
        elif row["V"] <= 3 * atrVL:
            vdf.loc[r, "vs"] = "XL"
        elif row["V"] <= 4 * atrVL:
            vdf.loc[r, "vs"] = "2XL"
        elif row["V"] <= 5 * atrVL:
            vdf.loc[r, "vs"] = "3XL"
        else:
            vdf.loc[r, "vs"] = "GIG"

    return vdf


# getVolumeCandleSize()
