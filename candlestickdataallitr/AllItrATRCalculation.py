import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from candlestickdata.CandleStickData import *
import math
from statistics import mean


def calculationAllItrForATR(sdf):
    # get previous Atr
    prvAtr = sdf['atr'][8]
    r = 9

    # ger last tr
    a = sdf["H"][r] - sdf["L"][r]
    b = abs(sdf["H"][r] - sdf["C"][r - 1])
    c = abs(sdf["L"][r] - sdf["C"][r - 1])
    lst = [a, b, c]
    tr = max(lst)

    # atr calculation
    atr = (prvAtr * 9 + tr) / 10
    atrPer = atr * 100 / sdf["C"][9]

    return atr, atrPer

# print(calculationForATR())