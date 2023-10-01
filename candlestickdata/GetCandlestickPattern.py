import time
import pandas as pd
import xlwings as xw
from candlestickdata.CandleStickData import *
from candlestickdata.ATRCalculation import *
from candlestickdata.GetCandleStickGender import *
from candlestickdata.GetCandlestickSize import *
from candlestickdata.GetCandlestickType import *
from concurrent.futures import ThreadPoolExecutor

tdf = pd.DataFrame()


def getCandlestickPattern():
    global tdf
    startTime = time.time()

    # get DataFrame
    tdf = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv")
    print(tdf)

    # get Pattern data
    def getPatternData(r):
        global tdf
        time.sleep(0.05)
        opnL = tdf[1][r]
        highL = tdf[2][r]
        lowL = tdf[3][r]
        clsL = tdf[4][r]
        atrL = tdf["atr"][r]
        gL = tdf["g"][r]
        sL = tdf["s"][r]
        tL = tdf["t"][r]

        # condition for reversal pattern
        # condition for triple candlestick pattern
        if r != 0 or r != 9:
            if tdf["g"][r-1] == "red" and tdf["t"][r] == "doji" and tdf["g"][r+1] == "green":
                tdf.iloc[r, "p"] = "morning_star"
        # condition for double candlestick pattern
        elif r != 0:
            # condition for tweezer bottom
            if tdf["g"][r-1] == "red" and tdf["g"][r] == "green":
                tdf.iloc[r, "p"] = "morning_star"

        elif r == 0 or r == 9:
            if tdf["t"][r] == "hammer":
                tdf.iloc[r, "p"] = "hammer"
            elif tdf["t"][r] == "shooting_star":
                tdf.iloc[r, "p"] = "shooting_star"

        # render data to xl

    # calculation for pattern
    with ThreadPoolExecutor() as executorOne:
        lt = list(range(10))
        executorOne.map(getPatternData, lt)

    print(tdf)
    tdf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv", index=False)
    print(f"time of execution is {time.time() - startTime}")


getCandlestickPattern()
