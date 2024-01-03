def getCandlestickSize(rangeS, atrS):
    if rangeS < 0.125 * atrS:
        return 0
    elif rangeS < 0.25 * atrS:
        return 0.25
    elif rangeS < 0.5*atrS:
        return 0.5
    elif rangeS < 0.75 * atrS:
        return 0.75
    elif rangeS < 1 * atrS:
        return 1
    elif rangeS < 1.5 * atrS:
        return 1.5
    elif rangeS < 2 * atrS:
        return 2
    elif rangeS < 3 * atrS:
        return 3
    elif rangeS < 4 * atrS:
        return 4
    else:
        return 5


# print(getCandlestickSize(9, 4))
