import math


def getBearishCandleLtpDistribution(rowX):
    # calculation for abc
    time = rowX['0']
    opn = rowX['1']
    high = rowX['2']
    low = rowX['3']
    close = rowX['4']
    ltpLst = list(range(61))
    ltpLst[0] = time
    if high > low:
        a = (high - opn) / (high - low)
        a = math.floor(a * 60)
        b = (opn - close) / (high - low)
        b = math.floor(b * 60)
    else:
        a = 20
        b = 20
    c = 60 - (a + b)
    aByTwo = math.floor(a / 2)
    cByTwo = math.floor(c / 2)
    for t in range(60):
        if t <= aByTwo:  # line one calculation
            m = (high - opn) / aByTwo
            ltp = opn + m * t
        elif t <= a:  # line two calculation
            m = (opn - high) / (a - aByTwo)
            ltp = high + m * (t - aByTwo)
        elif t <= a + b:
            m = (close - opn) / b
            ltp = opn + m * (t - a)
        elif t <= a + b + cByTwo:
            m = (low - close) / cByTwo
            ltp = close + m * (t - a - b)
        else:
            m = (close - low) / (c - cByTwo)
            ltp = low + m(t - a - b - cByTwo)
        ltpLst[t + 1] = ltp
    return ltpLst
