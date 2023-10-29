from candlestickdata.ATRCalculation import *
from concurrent.futures import ThreadPoolExecutor

tdg = pd.DataFrame()


def getAllItrBearishReversalCandlestickPattern(cdg):
    global tdg

    # get DataFrame
    tdg = cdg

    # get Pattern data
    def getAllItrBearishReversalPatternData(r):
        global tdg
        # condition for double candlestick pattern
        if tdg["t"][r] == "shooting_star":
            tdg.loc[r, "berRP"] = "shooting_star"
            return

        # condition for double candlestick pattern
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
        if r != 9:
            if tdg["g"][r - 1] == "green" and tdg["t"][r] == "doji" and tdg["g"][r + 1] == "red":
                tdg.loc[r, "berRP"] = "evening_star"

    # calculation for pattern
    with ThreadPoolExecutor() as executorOne:
        lt = [8, 9]
        executorOne.map(getAllItrBearishReversalPatternData, lt)

    return tdg


# getBearishReversalCandlestickPattern()
