import datetime
import pandas as pd
from commonudm.GetterTimeDelta import getterTimeDelta


def setPrePastTimeByMin(isLive=False):
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    ct = datetime.datetime.now() - cv
    ct = ct.strftime("%Y-%m-%d %H:%M:00")
    df = pd.DataFrame([ct], columns=['time'])
    df.to_csv(
        "F:\\AT\\commonudm\\resource\\PastTimeByMin.csv", index=False)


# setPrePastTimeByMin()
