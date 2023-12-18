def getCandleStickGender(opn, cls):
    gender = cls - opn
    if cls == 0:
        return "gap"
    elif gender >= 0:
        return "green"
    else:
        return "red"

# print(getCandleStickGender(2, 8))
