def getCandleStickGender(opn, cls):
    gender = cls - opn
    if gender >= 0:
        return "Green"
    else:
        return "Red"


# print(getCandleStickGender(2, 8))
