import datetime
import multiprocessing
import time

import pandas as pd

from belliprogressionem.GetterETStrategyFlag import getterETStrategyFlag
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetStackedETList import getStackedETList
from entry.GetterAppendAndSetterEntryList import getterAppendAndSetterEntryList
from entry.GetterECBList import getterECBList
from entry.GetterETLiveActionFlag import getterETLiveActionFlag
from entry.GetterUpdateAndSetterECBList import getterUpdateAndSetterECBList
from entry.LongPositionCalculator import longPositionCalculator
from entry.ShortPositionCalculator import shortPositionCalculator
from entrytriggeredlist.GetterDropAndSetterEntryTriggeredList import getterDropAndSetterEntryTriggeredList
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET
from ltpdistribution.GetLTPFromDistribution import getLTPFromDistribution
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket


def getEntryList(lock=multiprocessing.Lock(), isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # getting live action flags and they should not be interacted with strategy
        while True:
            try:
                eTBF, eTSF = getterETLiveActionFlag()
                break
            except Exception as e:
                print(f"exception while getting  eTBF, eTSF is {e}")

        # getter entry flags from the belli progressionem
        # ebf, esf = getEntryFlagUsingTrendingStrategy(cv, isLive)
        ebf, esf = getterETStrategyFlag()

        # getter Entry calculated and entry happened black list
        eCBLDf = getterECBList()

        # getter ET list
        eTDf = getStackedETList()

        for index, row in eTDf.iterrows():
            uid = row['id']
            if row['srV'] > 240:    # it is a time in seconds for which stack applies
                with lock:
                    # condition for removal of df
                    getterUpdateAndSetterBlackListET(uid, 0)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
            else:
                sector = row['sector']
                symbol = row['symbol']
                token = row['token']
                atr = row['atr']
                margin = 5
                ot = row['ot']
                if isLive:
                    ltp = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token).loc[0, '4']
                else:
                    ltp = getLTPFromDistribution(uid, cv)
                if eCBLDf.loc[uid - 1, 'eCBFlag'] == 1 or ltp == 0:
                    continue
                else:
                    if ot == 'buy' and eTBF == "F" and ebf == 'F':
                        q, sl, target = longPositionCalculator(ltp, atr, 1000, 1.2, 100000, margin, 1.5)
                        lp = 1.00025 * ltp

                        # calculation for margin required
                        # mr = abs(lp * q / margin)

                        upList = [0, uid, sector, symbol, token, ot, ltp, lp, q, sl, target, 0, 'open', 'open', '', 0, 0,
                                  0,
                                  row['oc'],
                                  time.time(), '', '', ltp]
                        with lock:
                            getterAppendAndSetterEntryList(upList)
                            getterUpdateAndSetterECBList(uid, 1)
                    elif ot == 'sell' and eTSF == "F" and esf == 'F':
                        q, sl, target = shortPositionCalculator(ltp, atr, 1000, 1.2, 100000, margin, 1.5)
                        lp = 0.99975 * ltp

                        # calculation for margin required
                        # mr = abs(lp * q / margin)

                        upList = [0, uid, sector, symbol, token, ot, ltp, lp, q, sl, target, 0, 'open', 'open', '', 0, 0,
                                  0,
                                  row['oc'],
                                  time.time(), '', '', ltp]
                        with lock:
                            getterAppendAndSetterEntryList(upList)
                            getterUpdateAndSetterECBList(uid, 1)

        # ctrA = ctrA + 1
        # if ctrA == 10:
        #     print(f"Execution time for getting Entry List (EL) is {time.time() - startTime}")
        #     ctrA = 0
        time.sleep(0.125)

# getEntryList()
