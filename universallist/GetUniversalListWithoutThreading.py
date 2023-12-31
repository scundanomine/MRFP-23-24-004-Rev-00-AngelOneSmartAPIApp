import time
import pandas as pd
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterNiftyDetailedListWithPivots import getterNiftyDetailedListWithPivots
from commonudm.GetterTimeDelta import getterTimeDelta
from traditionalpivotalarm.GetterPivotData import getterPivotData
from universallist.CondenseGSTData import condenseGSTData
from universallist.GetterDfThree import getterDfThree
import multiprocessing
import datetime


def getUniversalListWithoutThreading(lock=multiprocessing.Lock()):
    startTime = time.time()
    with lock:
        cv = getterTimeDelta()
        exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        with lock:
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
            result = condenseGSTData(uid, symbol, lock)
            dfThree.loc[index] = result

        # join of three df
        dfm = pd.merge(ndf, dfThree, left_index=True, right_index=True, how='outer')
        dfU = pd.merge(dfm, dcs, left_index=True, right_index=True, how='outer')

        # setting order type and it value can be buy or sell or null
        dfU['ot'] = ""

        # setting order characteristics and its value depends on the type of entry triggered
        dfU["oc"] = ""

        # save the list
        lock.acquire()
        dfU.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\universallist\\liststate\\UniversalList.csv",
            index=False)
        lock.release()
        print(f"Execution time for Universal list (UL) is {time.time() - startTime}")
        time.sleep(3.8)


# getUniversalListWithoutThreading()
