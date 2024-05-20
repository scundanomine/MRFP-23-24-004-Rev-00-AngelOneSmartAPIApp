from entry.GetterETLiveActionFlagDf import getterETLiveActionFlagDf
from exit.GetterExitLiveActionFlagDf import getterExitLiveActionFlagDf
from positionportfolioandmargindisplay.GetterEntryBannedDf import getterEntryBannedDf
from positionportfolioandmargindisplay.SetValueForEntryAndExitOption import setValueForEntryAndExitOption


def setETLiveAndEntryBannedParameters(lbf="T", lsf="T", lbExF="T", lsExF="T", optionEntry='All', optionExit='All', warningMsg=""):
    dfL = getterETLiveActionFlagDf()
    dfL.loc[0, "eTBF"] = lbf
    dfL.loc[0, "eTSF"] = lsf
    dfL.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ETLAFlag.csv",
        index=False)
    dfEx = getterExitLiveActionFlagDf()
    dfEx.loc[0, "eXBF"] = lbExF
    dfEx.loc[0, "eXSF"] = lsExF
    dfEx.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\EXLAFlag.csv",
        index=False)
    setValueForEntryAndExitOption(optionEntry, optionExit, warningMsg)

# setETLiveAndEntryBannedParameters(lbf="F", lsf="F", optionEntry='Default', optionExit='Default', rf=0, trend="none")
