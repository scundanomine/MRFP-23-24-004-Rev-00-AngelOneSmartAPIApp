from candlestickdata.ATRCalculation import *
from concurrent.futures import ThreadPoolExecutor

tdf = pd.DataFrame()


def getAllItrBullishReversalCandlestickPattern(cdf):
    global tdf

    # get DataFrame
    tdf = cdf

    # get Pattern data
    def getAllItrBullishReversalPatternData(r):
        global tdf

        # condition for double candlestick pattern
        if tdf["t"][r] == "hammer":
            tdf.loc[r, "bulRP"] = "hammer"
            return

        # condition for double candlestick pattern
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
        if r != 9:
            if tdf["g"][r-1] == "red" and tdf["t"][r] == "doji" and tdf["g"][r+1] == "green":
                tdf.loc[r, "bulRP"] = "morning_star"

    # calculation for pattern
    with ThreadPoolExecutor() as executorOne:
        lt = [8, 9]
        executorOne.map(getAllItrBullishReversalPatternData, lt)

    return tdf


# getBullishReversalCandlestickPattern()
