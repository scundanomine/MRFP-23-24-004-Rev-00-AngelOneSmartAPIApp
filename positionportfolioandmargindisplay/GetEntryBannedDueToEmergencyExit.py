import datetime
import time
from commonudm.GetterPastTimeByMin import getterPastTimeByMin
from commonudm.GetterTimeDelta import getterTimeDelta
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from positionportfolioandmargindisplay.GetterEntryBannedDf import getterEntryBannedDf
from positionportfolioandmargindisplay.GetterPastTimeByMinForEntryBanned import getterPastTimeByMinForEntryBanned
from positionportfolioandmargindisplay.SetETLiveAndEntryBannedParameters import setETLiveAndEntryBannedParameters


def getEntryBannedDueToEmergencyExit(cv):
    # getter initial past time by min
    dfPt = getterPastTimeByMinForEntryBanned()
    pt = dfPt.loc[0, 'time']
    ct = datetime.datetime.now() - cv
    ct = ct.strftime("%Y-%m-%d %H:%M:00")
    if ct != pt:
        time.sleep(2)
        df = getterMarketStructureDf()
        mTyp = df.loc[9, 'mTyp']
        dfc = getterEntryBannedDf()
        rf = dfc.loc[0, 'rf']
        trend = dfc.loc[0, 'trend']
        if rf != 0:
            if time.time() - rf >= 120 or mTyp != trend:
                setETLiveAndEntryBannedParameters()
        dfPt.loc[0, 'time'] = ct
        dfPt.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\positionportfolioandmargindisplay\\displaystate\\PastTimeByMinEB.csv",
            index=False)


# cpv = getterTimeDelta()
# getEntryBannedDueToEmergencyExit(cpv)
