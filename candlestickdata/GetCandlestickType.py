def getCandlestickType(b, us, ls, size):
    # range calculation
    r = b + us + ls
    # condition for doji
    if size == 0:
        return "doji"
    # condition for marubozu
    elif b >= 0.85 * r:
        return "marubozu"
    # condition for spn_top
    elif us >= 0.3 * r and ls >= 0.3 * r and b <= 0.25 * r:
        return "spn_top"
    # condition for hammer
    elif ls >= 0.6 * r:
        return "hammer"
    # condition for tweezer_b
    elif ls >= 0.5 * r:
        return "tweezer_b"
    # condition for shooting_star
    elif us >= 0.6 * r:
        return "shooting_star"
    # condition for tweezer_t
    elif us >= 0.5 * r:
        return "tweezer_t"
    else:
        return 'normal'

# print(getCandlestickType(4, 0.1, 0.011, "x"))
