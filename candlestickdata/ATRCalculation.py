import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from candlestickdata.CandleStickData import *
import math
from statistics import mean

df = []


def calculationForATR(sdf):
    global df
    df = sdf

    # print(df)
    # startTime = time.time()

    def getTR(r):
        try:
            global df
            # avg = (df["O"][r] + df["C"][r]) / 2
            if r == 0:
                tr = df["H"][r] - df["L"][r]
            else:
                a = df["H"][r] - df["L"][r]
                b = abs(df["H"][r] - df["C"][r - 1])
                c = abs(df["L"][r] - df["C"][r - 1])
                lst = [a, b, c]
                tr = max(lst)
            # print(f"for given r:{r}, tr is {tr}")

            # return tr/avg*100
            return tr
        except:
            return 0

    with ThreadPoolExecutor() as executor:
        lt = list(range(10))
        # print(lt)
        results = executor.map(getTR, lt)
        atr = mean(results)
        atrPercentile = atr*100/df["C"][9]
    # print(f"time of execution is {time.time() - startTime}")
    # return round(atr, 2), round(atrPercentile, 3)
    return atr, atrPercentile

# print(calculationForATR())
