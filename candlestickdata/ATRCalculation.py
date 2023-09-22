import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from candlestickdata.CandleStickData import *
import math
from statistics import mean

df = []


def calculationForATR():
    global df
    df = pd.DataFrame(getCandleStickData())
    print(df)
    startTime = time.time()

    def getTR(r):
        try:
            global df
            avg = (df[1][r] + df[4][r])/2
            if r == 0:
                tr = df[2][r] - df[3][r]
            else:
                a = df[2][r] - df[3][r]
                b = abs(df[2][r] - df[4][r - 1])
                c = abs(df[3][r] - df[4][r - 1])
                lst = [a, b, c]
                tr = max(lst)
            # print(f"for given r:{r}, tr is {tr}")
            return tr/avg*100
        except:
            return 0

    with ThreadPoolExecutor() as executor:
        lt = list(range(10))
        # print(lt)
        results = executor.map(getTR, lt)
        atr = mean(results)
    print(f"time of execution is {time.time() - startTime}")
    return atr


print(calculationForATR())
