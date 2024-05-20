import datetime
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket


def getPartlyCandleLengthAndGenderFromWebSocket(token, trg=False):
    # startTime = time.time()
    # get time
    refDate = datetime.datetime.now()
    ts = refDate.strftime("%S")
    if int(ts) < 15 and trg:
        return 0, 'none'
    df = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token)
    initialLtp = df.loc[0, "1"]
    finalLtp = df.loc[0, '4']
    try:
        if finalLtp < initialLtp:
            pcg = "red"
        else:
            pcg = "green"
        return abs(finalLtp - initialLtp), pcg
    except:
        return 0, 'none'


# print(getPartlyCandleLengthAndGenderFromWebSocket(99926000, True))
