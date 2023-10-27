from candlestickdata.ATRCalculation import *
from concurrent.futures import ThreadPoolExecutor

tdg = pd.DataFrame()


def getBearishReversalCandlestickPattern(cdg):
    global tdg

    # get DataFrame
    tdg = cdg
    tdg["berRP"] = "none"

    # get Pattern data
    def getBearishReversalPatternData(r):
        global tdg
        # condition for double candlestick pattern
        if tdg["t"][r] == "shooting_star":
            tdg.loc[r, "berRP"] = "shooting_star"
            return

        # condition for double candlestick pattern
        if r != 0:
            if tdg["g"][r - 1] == "green" and tdg["g"][r] == "red":
                # condition for tweezer bottom
                if tdg["t"][r - 1] == "tweezer_t" and tdg["t"][r] == "tweezer_t" and (tdg["O"][r]-tdg["C"][r-1]) <= 0.25*tdg["atr"][r]:
                    tdg.loc[r, "berRP"] = "tweezer_top"
                    return
                # condition for Dark Cloud Cover Pattern
                elif tdg["O"][r - 1] < tdg["C"][r] and (tdg["O"][r]-tdg["C"][r-1]) <= 0.25*tdg["atr"][r]:
                    tdg.loc[r, "berRP"] = "dark_cloud_cover"
                    return
                    # condition for Bearish Engulfing Pattern
                elif tdg["O"][r - 1] > tdg["C"][r] and (tdg["O"][r]-tdg["C"][r-1]) <= 0.25*tdg["atr"][r]:
                    tdg.loc[r, "berRP"] = "Bearish_Engulfing"
                    return

        # condition for triple candlestick pattern
        if r != 0 or r != 9:
            if tdg["g"][r - 1] == "green" and tdg["t"][r] == "doji" and tdg["g"][r + 1] == "red":
                tdg.loc[r, "berRP"] = "evening_star"

    # calculation for pattern
    with ThreadPoolExecutor() as executorOne:
        lt = list(range(10))
        executorOne.map(getBearishReversalPatternData, lt)

    return tdg


# getBearishReversalCandlestickPattern()
