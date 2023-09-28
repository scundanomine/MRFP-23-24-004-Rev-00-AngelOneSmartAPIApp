def getCandleStickGender(opn, cls):
    gender = cls - opn
    if gender >= 0:
        return "BLS"
    else:
        return "BRS"


# print(getCandleStickGender(2, 8))
