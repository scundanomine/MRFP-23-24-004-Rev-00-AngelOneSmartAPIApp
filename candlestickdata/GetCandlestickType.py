def getCandlestickType(b, us, ls, size):
    # range calculation
    r = b + us + ls
    # condition for doji
    if size == "zero":
        return "doji"
    # condition for marubozu
    elif b >= 0.9 * r:
        return "marubozu"
    # condition for spn_top
    elif us >= 2 * b and ls >= 2 * b:
        return "spn_top"
    # condition for hammer
    elif us <= 0.125 * r and b <= 0.25 * r:
        return "hammer"
    # condition for tweezer_t
    elif us <= 0.125 * r and b <= 0.6 * r:
        return "tweezer_t"
    # condition for shooting_star
    elif ls <= 0.125 * r and b <= 0.25 * r:
        return "shooting_star"
    # condition for tweezer_b
    elif ls <= 0.125 * r and b <= 0.6 * r:
        return "tweezer_b"
    else:
        return 'normal'


# print(getCandlestickType(4, 0.1, 0.011, "x"))
