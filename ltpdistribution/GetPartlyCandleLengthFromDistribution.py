import datetime
import time
from ltpdistribution.GetterSpecificDistributionDf import getterSpecificDistributionDf


def getPartlyCandleLengthAndGenderFromDistribution(uid, cv, trg=False):
    # startTime = time.time()
    df = getterSpecificDistributionDf(uid)
    df.set_index("time", inplace=True)
    # get time
    refDate = datetime.datetime.now() - cv + datetime.timedelta(minutes=1)
    ts = refDate.strftime("%S")
    if int(ts) < 15 and trg:
        return 0, 'none'
    reqTime = refDate.strftime("%Y-%m-%d %H:%M:00")
    initialLtp = df.loc[reqTime, '0']
    # print(time.time() - startTime)
    # getting required ohlc
    # pcg is partly candle gender
    try:
        finalLtp = df.loc[reqTime, str(ts)]
        if finalLtp < initialLtp:
            pcg = "red"
        else:
            pcg = "green"
        return abs(finalLtp - initialLtp), pcg
    except:
        ts = int(ts)
        finalLtp = df.loc[reqTime, str(ts)]
        if finalLtp < initialLtp:
            pcg = "red"
        else:
            pcg = "green"
        return abs(finalLtp - initialLtp), pcg


# cvs = getterTimeDelta()
# print(getLTPFromDistribution(1, cvs))
