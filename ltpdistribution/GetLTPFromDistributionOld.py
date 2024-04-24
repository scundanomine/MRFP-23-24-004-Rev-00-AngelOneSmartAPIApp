import datetime
from commonudm.GetterTimeDelta import getterTimeDelta
from ltpdistribution.GetterSpecificDistributionDf import getterSpecificDistributionDf


def getLTPFromDistributionOld(uid, cv):
    # getter fds and fFds
    df = getterSpecificDistributionDf("specificdistributiondf", uid)
    # cv = getterTimeDelta()
    # get time
    refDate = datetime.datetime.now() - cv + datetime.timedelta(minutes=1)
    ts = str(refDate.strftime("%S"))
    reqTime = refDate.strftime("%Y-%m-%dT%H:%M:00+05:30")

    # getting required ohlc
    if df.loc[0, 'time'] == reqTime:
        ltp = df.loc[0, ts]
    else:
        ltp = df.loc[1, ts]
    return ltp


# print(getLTPFromDistribution(11))
