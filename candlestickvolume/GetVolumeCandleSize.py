import pandas as pd
from concurrent.futures import ThreadPoolExecutor

atrVL = 0
vdf = pd.DataFrame()


def getVolumeCandleSize(df):
    global atrVL, vdf
    # get ATR
    atrVL = df["atrV"][9]

    # get df
    vdf = df

    def getIndividualVolumeCandlestickSize(r):
        global atrVL, vdf
        if vdf["V"][r] <= 0.125 * atrVL:
            vdf.loc[r, "vs"] = "zero"
        elif vdf["V"][r] <= 0.5 * atrVL:
            vdf.loc[r, "vs"] = "S"
        elif vdf["V"][r] <= atrVL:
            vdf.loc[r, "vs"] = "M"
        elif vdf["V"][r] <= 2 * atrVL:
            vdf.loc[r, "vs"] = "L"
        elif vdf["V"][r] <= 3 * atrVL:
            vdf.loc[r, "vs"] = "XL"
        elif vdf["V"][r] <= 4 * atrVL:
            vdf.loc[r, "vs"] = "2XL"
        elif vdf["V"][r] <= 5 * atrVL:
            vdf.loc[r, "vs"] = "3XL"
        else:
            vdf.loc[r, "vs"] = "GIG"

    with ThreadPoolExecutor() as executor:
        lt = list(range(10))
        executor.map(getIndividualVolumeCandlestickSize, lt)

    return vdf


# getVolumeCandleSize()
