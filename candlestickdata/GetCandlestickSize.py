def getCandlestickSize(body, atr):
    if body <= 0.125 * atr:
        return "zero"
    elif body <= 0.25 * atr:
        return "S"
    elif body <= 0.5 * atr:
        return "M"
    elif body <= atr:
        return "L"
    elif body <= 2 * atr:
        return "XL"
    elif body <= 3 * atr:
        return "2XL"
    else:
        return "GIG"


# print(getCandlestickSize(9, 4))
