from candlestickdata.ATRCalculation import *
from concurrent.futures import ThreadPoolExecutor

tdf = pd.DataFrame()


def getBullishReversalCandlestickPattern():
    global tdf
    startTime = time.time()

    # get DataFrame
    tdf = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv")
    tdf["p"] = "none"
    print(tdf)

    # get Pattern data
    def getBullishReversalPatternData(r):
        global tdf
        time.sleep(0.05)

        # condition for double candlestick pattern
        if tdf["t"][r] == "hammer":
            tdf.loc[r, "p"] = "hammer"
            return

        # condition for double candlestick pattern
        if r != 0:
            if tdf["g"][r - 1] == "red" and tdf["g"][r] == "green":
                # condition for tweezer bottom
                if tdf["t"][r - 1] == "tweezer_b" and tdf["t"][r] == "tweezer_b":
                    tdf.loc[r, "p"] = "tweezer_bottom"
                    return
                # condition for Piercing Pattern
                elif tdf["O"][r - 1] > tdf["C"][r]:
                    tdf.loc[r, "p"] = "Piercing"
                    return
                    # condition for Bullish Engulfing Pattern
                elif tdf["O"][r - 1] < tdf["C"][r]:
                    tdf.loc[r, "p"] = "Bullish_Engulfing"
                    return

        # condition for triple candlestick pattern
        if r != 0 or r != 9:
            if tdf["g"][r-1] == "red" and tdf["t"][r] == "doji" and tdf["g"][r+1] == "green":
                tdf.loc[r, "p"] = "morning_star"

    # calculation for pattern
    with ThreadPoolExecutor() as executorOne:
        lt = list(range(10))
        executorOne.map(getBullishReversalPatternData, lt)

    print(tdf)
    tdf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv", index=False)
    print(f"time of execution is {time.time() - startTime}")


getBullishReversalCandlestickPattern()
