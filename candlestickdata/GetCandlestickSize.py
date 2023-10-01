def getCandlestickSize(rangeS, atrS):
    # rangeS = rangeS*10000
    # atrS = atrS * 10000
    if rangeS <= 0.25 * atrS:
        return "zero"
    elif rangeS <= 0.5 * atrS:
        return "S"
    elif rangeS <= atrS:
        return "M"
    elif rangeS <= 1.5 * atrS:
        return "L"
    elif rangeS <= 2.5 * atrS:
        return "XL"
    elif rangeS <= 3.5 * atrS:
        return "2XL"
    else:
        return "GIG"


# print(getCandlestickSize(9, 4))
