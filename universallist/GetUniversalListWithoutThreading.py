import datetime
import time
import pandas as pd
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterNiftyDetailedListWithPivots import getterNiftyDetailedListWithPivots
from commonudm.GetterTimeDelta import getterTimeDelta
from traditionalpivotalarm.GetterPivotData import getterPivotData
from universallist.CondenseGSTData import condenseGSTData
from universallist.GetterDfThree import getterDfThree


def getUniversalListWithoutThreading(isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # nifty detailed list
        ndf = getterNiftyDetailedListWithPivots()
        # dcs and dcs list
        dcs = getterPivotData()
        dcs = dcs.loc[:, ['alarmTimer', 'srT', 'srV', 'nSR', 'GL']]
        # print(dcs)

        # creation of df three
        dfThree = getterDfThree()

        # define sub function
        for index, row in ndf.iterrows():
            uid = row['id']
            symbol = row['symbol']
            result = condenseGSTData(uid, symbol)
            dfThree.loc[index] = result

        # join of three df
        dfm = pd.merge(ndf, dfThree, left_index=True, right_index=True, how='outer')
        dfU = pd.merge(dfm, dcs, left_index=True, right_index=True, how='outer')

        # setting order type and it value can be buy or sell or null
        dfU['ot'] = ""

        # setting order characteristics and its value depends on the type of entry triggered
        dfU["oc"] = ""

        # save the list
        dfU.to_csv(
                "F:\\AT\\universallist\\liststate\\UniversalList.csv",
                index=False)
        # ctrA = ctrA + 1
        # if ctrA == 10:
        #     print(f"Execution time for Universal list (UL) is {time.time() - startTime}")
        #     ctrA = 0
        time.sleep(0.125)


# getUniversalListWithoutThreading()
