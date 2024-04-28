from entry.GetterETLiveActionFlagDf import getterETLiveActionFlagDf
from positionportfolioandmargindisplay.GetterEntryBannedDf import getterEntryBannedDf
from positionportfolioandmargindisplay.SetValueForEntryAndExitOption import setValueForEntryAndExitOption


def setETLiveAndEntryBannedParameters(lbf="F", lsf="F", optionEntry='Default', optionExit='Default', rf=0,
                                      trend="none"):
    dfL = getterETLiveActionFlagDf()
    dfL.loc[0, "eTBF"] = lbf
    dfL.loc[0, "eTSF"] = lsf
    dfL.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ETLAFlag.csv",
        index=False)
    setValueForEntryAndExitOption(optionEntry, optionExit)
    df = getterEntryBannedDf()
    df[0, 'rf'] = rf
    df[0, 'trend'] = trend
    df.to_csv(
        'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\positionportfolioandmargindisplay\\displaystate\\EntryBanned.csv',
        index=False)
    print(lbf, lsf, optionEntry, optionExit)


# setETLiveAndEntryBannedParameters(lbf="F", lsf="F", optionEntry='Default', optionExit='Default', rf=0, trend="none")
