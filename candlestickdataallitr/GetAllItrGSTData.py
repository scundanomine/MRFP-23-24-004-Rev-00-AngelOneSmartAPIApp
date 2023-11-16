from candlestickdata.GetCandleStickGender import *
from candlestickdata.GetCandlestickSize import *
from candlestickdata.GetCandlestickType import *


def getAllItrCandlestickGSTData(gdf):
    sdf = gdf
    r = 9

    # get gst data
    opnL = sdf["O"][r]
    highL = sdf["H"][r]
    lowL = sdf["L"][r]
    clsL = sdf["C"][r]
    atrL = sdf["atr"][r]

    # calculation for gender
    g = getCandleStickGender(opnL, clsL)

    # calculation for size
    bodyL = opnL - clsL
    rangeL = highL - lowL
    s = getCandlestickSize(rangeL, atrL)

    # calculation for type, here us is upper shadow and ls is lower shadow and L prefix is used for the local.
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

    return sdf

# getCandlestickGSTData()
