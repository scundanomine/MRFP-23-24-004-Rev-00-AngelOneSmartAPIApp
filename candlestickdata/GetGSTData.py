from candlestickdata.ATRCalculation import *
from candlestickdata.GetCandleStickGender import *
from candlestickdata.GetCandlestickSize import *
from candlestickdata.GetCandlestickType import *
from concurrent.futures import ThreadPoolExecutor

sdf = pd.DataFrame()


def getCandlestickGSTData(gdf):
    global sdf

    sdf = gdf

    # get gst data
    def getGstData(r):
        global sdf
        opnL = sdf["O"][r]
        highL = sdf["H"][r]
        lowL = sdf["L"][r]
        clsL = sdf["C"][r]
        atrL = sdf["atr"][r]

        # calculation for gender and gender can green, red and gap
        g = getCandleStickGender(opnL, clsL)

        # calculation for size
        bodyL = opnL - clsL
        rangeL = highL - lowL
        s = getCandlestickSize(rangeL, atrL)

        # calculation for type
        if g == 'green':
            usL = highL - clsL
            lsL = opnL - lowL
        else:
            usL = highL - opnL
            lsL = clsL - lowL
        t = getCandlestickType(abs(bodyL), usL, lsL, s)

        # render gst data to the dataFrame
        sdf.loc[r, "g"] = g
        sdf.loc[r, "s"] = s
        sdf.loc[r, "t"] = t

    # calculation for gst data
    with ThreadPoolExecutor() as executor:
        lt = list(range(10))
        executor.map(getGstData, lt)

    # print(sdf)
    # sdf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\candlestickdata\\candle_state\\gstData.csv", index=False)
    return sdf


# getCandlestickGSTData()
