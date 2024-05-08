from candlestickdata.GetCandleStickGender import *
from candlestickdata.GetCandlestickSize import *
from candlestickdata.GetCandlestickType import *


def getAllItrCandlestickGSTData(sdf):
    r = 9
    if sdf.loc[9, 'C'] != 0:
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
    else:
        sdf.loc[r, "g"] = "none"
        sdf.loc[r, "s"] = 0
        sdf.loc[r, "t"] = "none"

        return sdf

# getCandlestickGSTData()
