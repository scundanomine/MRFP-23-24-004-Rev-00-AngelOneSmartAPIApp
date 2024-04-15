import math


def getBullishCandleLtpDistribution(rowX):
    # calculation for abc
    time = rowX['0']
    opn = rowX['1']
    high = rowX['2']
    low = rowX['3']
    close = rowX['4']
    ltpLst = list(range(61))
    ltpLst[0] = time
    if high > low:
        a = (opn - low) / (high - low)
        a = math.floor(a * 60)
        b = (close - opn) / (high - low)
        b = math.floor(b * 60)
    else:
        a = 20
        b = 20
    c = 60 - (a + b)
    aByTwo = math.floor(a / 2)
    cByTwo = math.floor(c / 2)
    for t in range(60):
        if t <= aByTwo and a > 1:  # line one calculation
            m = (low - opn) / aByTwo
            ltp = opn + m * t
        elif t <= a and a > 1:  # line two calculation
            m = (opn - low) / (a - aByTwo)
            ltp = low + m * (t - aByTwo)
        elif t <= a + b and b != 0:
            m = (close - opn) / b
            ltp = opn + m * (t - a)
        elif t <= a + b + cByTwo and c > 1:
            m = (high - close) / cByTwo
            ltp = close + m * (t - a - b)
        elif t <= a + b + c and c > 1:
            m = (close - high) / (c - cByTwo)
            ltp = high + m * (t - a - b - cByTwo)
        else:
            ltp = rowX['4']
        ltpLst[t + 1] = ltp
    return ltpLst
