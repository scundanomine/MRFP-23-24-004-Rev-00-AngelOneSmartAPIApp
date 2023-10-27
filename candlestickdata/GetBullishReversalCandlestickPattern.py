from candlestickdata.ATRCalculation import *
from concurrent.futures import ThreadPoolExecutor

tdf = pd.DataFrame()


def getBullishReversalCandlestickPattern(cdf):
    global tdf

    # get DataFrame
    tdf = cdf
    tdf["bulRP"] = "none"
    # print(tdf)

    # get Pattern data
    def getBullishReversalPatternData(r):
        global tdf

        # condition for double candlestick pattern
        if tdf["t"][r] == "hammer":
            tdf.loc[r, "bulRP"] = "hammer"
            return

        # condition for double candlestick pattern
        if r != 0:
            if tdf["g"][r - 1] == "red" and tdf["g"][r] == "green":
                # condition for tweezer bottom
                if tdf["t"][r - 1] == "tweezer_b" and tdf["t"][r] == "tweezer_b" and tdf["C"][r-1] - tdf["O"][r] <= 0.25*tdf["atr"][r]:
                    tdf.loc[r, "bulRP"] = "tweezer_bottom"
                    return
                # condition for Piercing Pattern
                elif tdf["O"][r - 1] > tdf["C"][r] and tdf["C"][r-1] - tdf["O"][r] <= 0.25*tdf["atr"][r]:
                    tdf.loc[r, "bulRP"] = "Piercing"
                    return
                    # condition for Bullish Engulfing Pattern
                elif tdf["O"][r - 1] < tdf["C"][r] and tdf["C"][r-1] - tdf["O"][r] <= 0.25*tdf["atr"][r]:
                    tdf.loc[r, "bulRP"] = "Bullish_Engulfing"
                    return

        # condition for triple candlestick pattern
        if r != 0 or r != 9:
            if tdf["g"][r-1] == "red" and tdf["t"][r] == "doji" and tdf["g"][r+1] == "green":
                tdf.loc[r, "bulRP"] = "morning_star"

    # calculation for pattern
    with ThreadPoolExecutor() as executorOne:
        lt = list(range(10))
        executorOne.map(getBullishReversalPatternData, lt)

    return tdf


# getBullishReversalCandlestickPattern()
