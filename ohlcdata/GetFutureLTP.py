import datetime
from commonudm.GetterTimeDelta import getterTimeDelta
from ohlcdata.GetterFDS import getterFDS
from ohlcdata.GetterFFDS import getterFFDS


def getFutureLTP(uid):
    # getter fds and fFds
    fds = getterFDS()
    fFds = getterFFDS()
    cv = getterTimeDelta()

    # getting required records
    recOne = fds.iloc[uid - 1]
    recTwo = fFds.iloc[uid - 1]

    # get time
    refDate = datetime.datetime.now() - cv + datetime.timedelta(minutes=1)
    reqTime = refDate.strftime("%Y-%m-%dT%H:%M:00+05:30")

    # getting required ohlc
    if reqTime == recOne['0']:
        op = recOne['1']
        h = recOne['2']
        lo = recOne['3']
        c = recOne['4']
    else:
        op = recTwo['1']
        h = recTwo['2']
        lo = recTwo['3']
        c = recTwo['4']

    # get the current time in sec
    curTime = datetime.datetime.now() - cv
    ts = int(curTime.strftime("%S"))

    # final condition for getting ltp
    if op <= c:
        if ts <= 20:
            ltp = op + (lo - op) / 20 * ts
        elif ts <= 40:
            ltp = lo + (h - lo) / 20 * (ts - 20)
        else:
            ltp = h + (c - h) / 20 * (ts - 40)
    else:
        if ts <= 20:
            ltp = op + (h - op) / 20 * ts
        elif ts <= 40:
            ltp = h + (lo - h) / 20 * (ts - 20)
        else:
            ltp = lo + (c - lo) / 20 * (ts - 40)
    return ltp


# getFutureLTP(67)
