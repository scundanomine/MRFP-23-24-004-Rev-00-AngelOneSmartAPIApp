import datetime
import time
from commonudm.GetterPastTimeByMin import getterPastTimeByMin
from positionportfolioandmargindisplay.GetterEntryBannedDf import getterEntryBannedDf
from positionportfolioandmargindisplay.SetETLiveAndEntryBannedParameters import setETLiveAndEntryBannedParameters


def getEntryBannedDueToEmergencyExit(cv):
    # getter initial past time by min
    dfPt = getterPastTimeByMin()
    pt = dfPt.loc[0, 'time']
    ct = datetime.datetime.now() - cv
    ct = ct.strftime("%Y-%m-%d %H:%M:00")
    if ct != pt:
        dfc = getterEntryBannedDf()
        rf = dfc[0, 'rf']
        if rf != 0:
            if time.time() - rf > 180:
                setETLiveAndEntryBannedParameters()

