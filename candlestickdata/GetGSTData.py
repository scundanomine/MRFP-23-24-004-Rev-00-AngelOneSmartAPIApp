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


def getCandlestickGSTData(gdf, atrS):
    global sdf

    # get DataFrame
    # sdf = pd.DataFrame(getCandleStickData())
    sdf = gdf
    startTime = time.time()

    # get atr
    # atr = round(calculationForATR(sdf), 2)
    # print(atr)
    atr = atrS

    # rename ohlc
    sdf.rename(columns={0: "time", 1: "O", 2: "H", 3: "L", 4: "C", 5: "V"}, inplace=True)
    # add required columns
    new_cols = ['atr', 'g', 's', 't', 'p', 'atrV', 'vs']
    cols_to_add = [col for col in new_cols if col not in sdf.columns]
    sdf.loc[:, cols_to_add] = 0
    sdf["atr"] = atr
    sdf["p"] = "none"

    # print(sdf.iloc[0])

    # get gst data
    def getGstData(r):
        global sdf
        time.sleep(0.05)
        opnL = sdf["O"][r]
        highL = sdf["H"][r]
        lowL = sdf["L"][r]
        clsL = sdf["C"][r]
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
