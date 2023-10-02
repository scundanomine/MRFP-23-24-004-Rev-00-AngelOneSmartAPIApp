from candlestickdata.ATRCalculation import *
from concurrent.futures import ThreadPoolExecutor

tdg = pd.DataFrame()


def getBearishReversalCandlestickPattern():
    global tdg
    startTime = time.time()

    # get DataFrame
    tdg = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv")
    tdg["p"] = "none"
    print(tdg)

    # get Pattern data
    def getBearishReversalPatternData(r):
        global tdg
        time.sleep(0.05)

        # condition for double candlestick pattern
        if tdg["t"][r] == "shooting_star":
            tdg.loc[r, "p"] = "shooting_star"
            return

        # condition for double candlestick pattern
        if r != 0:
            if tdg["g"][r - 1] == "green" and tdg["g"][r] == "red":
                # condition for tweezer bottom
                if tdg["t"][r - 1] == "tweezer_t" and tdg["t"][r] == "tweezer_t":
                    tdg.loc[r, "p"] = "tweezer_top"
                    return
                # condition for Dark Cloud Cover Pattern
                elif tdg[1][r - 1] < tdg[4][r]:
                    tdg.loc[r, "p"] = "dark_cloud_cover"
                    return
                    # condition for Bearish Engulfing Pattern
                elif tdg[1][r - 1] > tdg[4][r]:
                    tdg.loc[r, "p"] = "Bearish_Engulfing"
                    return

        # condition for triple candlestick pattern
        if r != 0 or r != 9:
            if tdg["g"][r - 1] == "green" and tdg["t"][r] == "doji" and tdg["g"][r + 1] == "red":
                tdg.loc[r, "p"] = "evening_star"

    # calculation for pattern
    with ThreadPoolExecutor() as executorOne:
        lt = list(range(10))
        executorOne.map(getBearishReversalPatternData, lt)

    print(tdg)
    tdg.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv", index=False)
    print(f"time of execution is {time.time() - startTime}")


getBearishReversalCandlestickPattern()
