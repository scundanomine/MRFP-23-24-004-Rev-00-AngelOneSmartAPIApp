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


def getCandlestickPattern():
    global sdf
    startTime = time.time()

    # get DataFrame
    sdf = pd.DataFrame(getCandleStickData())

    # get atr
    atr = round(calculationForATR(sdf), 2)
    print(atr)

    # add required columns
    new_cols = ['atr', 'g', 's', 't', 'p']
    cols_to_add = [col for col in new_cols if col not in sdf.columns]
    sdf.loc[:, cols_to_add] = 0
    sdf["atr"] = atr
    print(sdf.iloc[0])

    # get gst data
    def getGstData(r):
        global sdf

        # calculation for gender
        opnL = sdf[1][r]
        clsL = sdf[4][r]
        g = getCandleStickGender(opnL, clsL)

        # calculation for size
        atrL = sdf[5][r]
        bodyL = opnL - clsL
        s = getCandlestickSize(abs(bodyL), atrL)

        # calculation for type
        highL = sdf[1][r]
        lowL = sdf[4][r]
        if g == 'BLS':
            pass

    # with ThreadPoolExecutor() as executor:
    #     lt = list(range(10))
    #     executor.map(getGstData, lt)


getCandlestickPattern()
