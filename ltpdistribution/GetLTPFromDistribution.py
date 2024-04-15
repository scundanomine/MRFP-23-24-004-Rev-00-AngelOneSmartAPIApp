import datetime
from commonudm.GetterTimeDelta import getterTimeDelta
from ltpdistribution.GetterSpecificDistributionDf import getterSpecificDistributionDf


def getLTPFromDistribution(uid, cv):
    # getter fds and fFds
    df = getterSpecificDistributionDf("specificdistributiondf", uid)
    # cv = getterTimeDelta()
    # get time
    refDate = datetime.datetime.now() - cv + datetime.timedelta(minutes=1)
    ts = int(refDate.strftime("%S"))
    reqTime = refDate.strftime("%Y-%m-%dT%H:%M:00+05:30")

    # getting required ohlc
    if df[0, 'time'] == reqTime:
        ltp = df[0, ts]
    else:
        ltp = df[1, ts]
    return ltp

# getLTPFromDistribution(67)
