from commonudm.GetterNiftyDetailedListWithPivots import getterNiftyDetailedListWithPivots
from traditionalpivotalarm.GetterPivotData import getterPivotData
from universallist.GetterDfThree import getterDfThree
import pandas as pd


def cleaningAndSettingUniversalList():
    ndf = getterNiftyDetailedListWithPivots()
    dcs = getterPivotData()
    dcs = dcs.loc[:, ['alarmTimer', 'srT', 'srV', 'nSR', 'GL']]
    # creation of df three
    dfThree = getterDfThree()
    # join of three df
    dfm = pd.merge(ndf, dfThree, left_index=True, right_index=True, how='outer')
    dfU = pd.merge(dfm, dcs, left_index=True, right_index=True, how='outer')

    # setting order type and it value can be buy or sell or null
    dfU['ot'] = ""

    # setting order characteristics and its value depends on the type of entry triggered
    dfU["oc"] = ""

    dfU.to_csv(
        "F:\\AT\\universallist\\liststate\\UniversalList.csv",
        index=False)

    # print(dfU)


# cleaningAndSettingUniversalList()
