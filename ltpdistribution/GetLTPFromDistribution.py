import datetime
from commonudm.GetterTimeDelta import getterTimeDelta
from ltpdistribution.GetterSpecificDistributionDfWithTime import getterPartlySpecificDistributionDf


def getLTPFromDistribution(uid, cv):
    df = getterPartlySpecificDistributionDf(uid)
    # get time
    refDate = datetime.datetime.now() - cv + datetime.timedelta(minutes=1)
    ts = refDate.strftime("%S")
    reqTime = refDate.strftime("%Y-%m-%d %H:%M")
    # getting required ohlc
    try:
        return df.loc[reqTime, ts]
    except:
        ts = int(ts)
        return df.loc[reqTime, str(ts)]


cvs = getterTimeDelta()
print(getLTPFromDistribution(11, cvs))
