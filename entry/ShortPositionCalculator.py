import math


def shortPositionCalculator(ltp, atr, mpl=500, rrr=1.2, lot=50000, margin=5, atrF=1.5):
    # calculation for quantity for stocks to be sold
    nOne = mpl / (atrF * atr)
    nTwo = margin * lot / ltp
    if nOne >= nTwo:
        q = math.floor(nTwo)
    else:
        q = math.floor(nOne)

    # calculation for sl and target
    sl = ltp + atrF * atr
    target = ltp - rrr * atrF * atr

    return q, sl, target


print(shortPositionCalculator(1000, 2))

