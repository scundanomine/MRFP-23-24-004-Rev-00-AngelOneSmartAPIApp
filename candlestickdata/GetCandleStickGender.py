def getCandleStickGender(opn, cls):
    gender = cls - opn
    if gender >= 0:
        return "green"
    else:
        return "red"


# print(getCandleStickGender(2, 8))
