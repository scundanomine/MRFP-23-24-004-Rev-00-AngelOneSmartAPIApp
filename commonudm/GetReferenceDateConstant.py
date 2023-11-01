import datetime


def getRefDateConstant(dateR):
    refDate = datetime.datetime.strptime(dateR, "%d %b %Y %H:%M:%S.%f")
    return datetime.datetime.now() - refDate
