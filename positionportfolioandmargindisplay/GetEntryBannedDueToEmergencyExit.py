import datetime
import time
from commonudm.GetterPastTimeByMin import getterPastTimeByMin
from entry.GetterETLiveActionFlagDf import getterETLiveActionFlagDf
from positionportfolioandmargindisplay.GetterEntryBannedDf import getterEntryBannedDf
from positionportfolioandmargindisplay.SetValueForEntryAndExitOption import setValueForEntryAndExitOption


def getEntryBannedDueToEmergencyExit(cv):
    # getter initial past time by min
    dfPt = getterPastTimeByMin()
    pt = dfPt.loc[0, 'time']
    ct = datetime.datetime.now() - cv
    ct = ct.strftime("%Y-%m-%d %H:%M:00")
    if ct != pt:
        df = getterEntryBannedDf()
        rf = df[0, 'rf']
        if rf != 0:
            if time.time() - rf > 180:
                dfL = getterETLiveActionFlagDf()
                dfL.loc[0, "eTBF"] = "F"
                dfL.loc[0, "eTSF"] = "F"
                dfL.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ETLAFlag.csv", index=False)
                setValueForEntryAndExitOption()
                df[0, 'rf'] = 0
                df[0, 'trend'] = "none"
                df.to_csv(
                    'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\positionportfolioandmargindisplay\\displaystate\\EntryBanned.csv',
                    index=False)

