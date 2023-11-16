from candlestickdata.CandleStickData import *
from statistics import mean

df = []


def calculationForATR(sdf):
    global df
    df = sdf

    def getTR(r):
        try:
            global df
            if r == 0:
                tr = df["H"][r] - df["L"][r]
            else:
                a = df["H"][r] - df["L"][r]
                b = abs(df["H"][r] - df["C"][r - 1])
                c = abs(df["L"][r] - df["C"][r - 1])
                lst = [a, b, c]
                tr = max(lst)
            return tr
        except:
            return 0

    with ThreadPoolExecutor() as executor:
        lt = list(range(10))
        # print(lt)
        results = executor.map(getTR, lt)
        atr = mean(results)

    # calculation for atr percentile
    maxPrice = df["C"].max()
    if maxPrice != 0:
        atrPercentile = atr * 100 / maxPrice
    else:
        atrPercentile = 0
    # print(f"time of execution is {time.time() - startTime}")
    # return round(atr, 2), round(atrPercentile, 3)
    return atr, atrPercentile

# print(calculationForATR())
