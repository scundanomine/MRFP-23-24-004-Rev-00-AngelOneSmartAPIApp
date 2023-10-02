import time
import pandas as pd
import xlwings as xw
from candlestickdata.CandleStickData import *
from candlestickdata.ATRCalculation import *
from candlestickdata.GetCandleStickGender import *
from candlestickdata.GetCandlestickSize import *
from candlestickdata.GetCandlestickType import *
from concurrent.futures import ThreadPoolExecutor

sdf = pd.DataFrame()


def getCandlestickGSTData():
    global sdf

    # get DataFrame
    sdf = pd.DataFrame(getCandleStickData())
    startTime = time.time()

    # get atr
    atr = round(calculationForATR(sdf), 2)
    print(atr)

    # add required columns
    new_cols = ['atr', 'g', 's', 't', 'p']
    cols_to_add = [col for col in new_cols if col not in sdf.columns]
    sdf.loc[:, cols_to_add] = 0
    sdf["atr"] = atr
    sdf["p"] = "none"

    # print(sdf.iloc[0])

    # get gst data
    def getGstData(r):
        global sdf
        time.sleep(0.05)
        opnL = sdf[1][r]
        highL = sdf[2][r]
        lowL = sdf[3][r]
        clsL = sdf[4][r]
        atrL = sdf["atr"][r]

        # calculation for gender
        g = getCandleStickGender(opnL, clsL)

        # calculation for size
        bodyL = opnL - clsL
        rangeL = highL - lowL
        s = getCandlestickSize(rangeL, atrL)

        # calculation for type
        if g == 'green':
            usL = highL - clsL
            lsL = opnL - lowL
        else:
            usL = highL - opnL
            lsL = clsL - lowL
        t = getCandlestickType(abs(bodyL), usL, lsL, s)

        # render gst data to the dataFrame
        sdf.loc[r, "g"] = g
        sdf.loc[r, "s"] = s
        sdf.loc[r, "t"] = t

    # calculation for gst data
    with ThreadPoolExecutor() as executor:
        lt = list(range(10))
        executor.map(getGstData, lt)

    print(sdf)
    sdf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv", index=False)
    print(f"time of execution is {time.time() - startTime}")


getCandlestickGSTData()
