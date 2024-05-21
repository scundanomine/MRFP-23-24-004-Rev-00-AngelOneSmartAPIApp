import datetime
import time
from ltpdistribution.GetterSpecificDistributionDf import getterSpecificDistributionDf


def getLTPFromDistribution(uid, cv):
    # startTime = time.time()
    df = getterSpecificDistributionDf(uid)
    df.set_index("time", inplace=True)
    # get time
    refDate = datetime.datetime.now() - cv
    ts = refDate.strftime("%S")
    reqTime = refDate.strftime("%Y-%m-%d %H:%M:00")
    # print(time.time() - startTime)
    # getting required ohlc
    try:
        return df.loc[reqTime, ts]
    except:
        ts = int(ts)
        return df.loc[reqTime, str(ts)]


# cvs = getterTimeDelta()
# print(getLTPFromDistribution(1, cvs))
