import time
import pandas as pd
from positionportfolioandmargindisplay.GetterEntryBannedDf import getterEntryBannedDf
from positionportfolioandmargindisplay.SetETLiveAndEntryBannedParameters import setETLiveAndEntryBannedParameters


def getEntryBannedDueToEmergencyExit(df=pd.DataFrame()):
    mTyp = df.loc[9, 'mTyp']
    dfc = getterEntryBannedDf()
    rf = dfc.loc[0, 'rf']
    trend = dfc.loc[0, 'trend']
    if rf != 0:
        if time.time() - rf >= 120 or mTyp != trend:
            setETLiveAndEntryBannedParameters()


# cpv = getterTimeDelta()
# getEntryBannedDueToEmergencyExit(cpv)
