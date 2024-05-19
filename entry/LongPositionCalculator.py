import math


def longPositionCalculator(ltp, atr, mpl=200, rrr=1.2, lot=20000, margin=5, atrF=1.5):
    # calculation for quantity for stocks to be bought
    # mpl is max. Permissible loss in one position
    nOne = mpl / (atrF * atr)
    nTwo = margin * lot / ltp
    if nOne >= nTwo:
        q = math.floor(nTwo)
    else:
        q = math.floor(nOne)

    # calculation for sl and target
    sl = ltp - 5 * atr
    target = ltp + rrr * atrF * atr

    if q == 0:
        q = 1

    return q, sl, target


# print(longPositionCalculator(1000, 2))
