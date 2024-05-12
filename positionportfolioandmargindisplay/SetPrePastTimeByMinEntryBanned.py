import datetime
import pandas as pd
from commonudm.GetterTimeDelta import getterTimeDelta


def setPrePastTimeByMinEntryBanned(isLive=False):
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    ct = datetime.datetime.now() - cv
    ct = ct.strftime("%Y-%m-%d %H:%M:00")
    df = pd.DataFrame([ct], columns=['time'])
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\positionportfolioandmargindisplay\\displaystate\\PastTimeByMinEB.csv", index=False)


# setPrePastTimeByMin()
