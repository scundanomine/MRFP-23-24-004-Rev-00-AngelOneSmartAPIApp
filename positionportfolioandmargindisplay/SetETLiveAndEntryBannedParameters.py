from entry.GetterETLiveActionFlagDf import getterETLiveActionFlagDf
from exit.GetterExitLiveActionFlagDf import getterExitLiveActionFlagDf
from positionportfolioandmargindisplay.GetterEntryBannedDf import getterEntryBannedDf
from positionportfolioandmargindisplay.SetValueForEntryAndExitOption import setValueForEntryAndExitOption


def setETLiveAndEntryBannedParameters(lbf="F", lsf="F", lbExF="F", lsExF="F", optionEntry='Default', optionExit='Default', rf=0,
                                      trend="none", pSize=1, warningMsg=""):
    if pSize != 0:
        # dfL = getterETLiveActionFlagDf()
        # dfL.loc[0, "eTBF"] = lbf
        # dfL.loc[0, "eTSF"] = lsf
        # dfL.to_csv(
        #     "F:\\AT\\entry\\entrystate\\ETLAFlag.csv",
        #     index=False)
        # dfEx = getterExitLiveActionFlagDf()
        # dfEx.loc[0, "eXBF"] = lbExF
        # dfEx.loc[0, "eXSF"] = lsExF
        # dfEx.to_csv(
        #     "F:\\AT\\exit\\exitstate\\EXLAFlag.csv",
        #     index=False)
        setValueForEntryAndExitOption(optionEntry, optionExit, warningMsg)
        df = getterEntryBannedDf()
        df.loc[0, 'rf'] = rf
        df.loc[0, 'trend'] = trend
        df.to_csv(
            'F:\\AT\\positionportfolioandmargindisplay\\displaystate\\EntryBanned.csv',
            index=False)
        # print(lbf, lsf, optionEntry, optionExit)


# setETLiveAndEntryBannedParameters(lbf="F", lsf="F", optionEntry='Default', optionExit='Default', rf=0, trend="none")
