from candlestickdata.GetCandleStickGender import *
from candlestickdata.GetCandlestickSize import *
from candlestickdata.GetCandlestickType import *


def getGSTDataWithoutThreading(sdf):
    for r, row in sdf.iterrows():
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
    return sdf


# getGSTDataWithoutThreading()
