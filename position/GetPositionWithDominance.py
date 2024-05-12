import datetime
import multiprocessing
import time

import pandas as pd

from belliprogressionem.bellientry.GetEntryFlagUsingTrendingStrategy import getEntryFlagUsingTrendingStrategy
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterReportDateForRR import getterReportDateForRR
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterDropAndSetterEntryList import getterDropAndSetterEntryList
from entry.GetterETLiveActionFlag import getterETLiveActionFlag
from entry.GetterEntryList import getterEntryList
from ltpdistribution.GetLTPFromDistribution import getLTPFromDistribution
from margin.GetterAvailableMargin import getterAvailableMargin
from margin.GetterDebitAndSetterAvailableMargin import getterDebitAndSetterAvailableMargin
from portfolio.GetterUpdateAndSetterFixedPortfolioWithExpenses import getterUpdateAndSetterFixedPortfolioWithExpenses
from position.GetEtAndEntryDropFunction import getEtAndEntryDropFunction
from position.GetterAppendAndSetterPositionList import getterAppendAndSetterPositionList
from position.GetterUpdateAndSetterPositionId import getterUpdateAndSetterPositionId
from readandrecord.SetPositionDetailsAndCandles import setPositionDetailsAndCandles
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket


def getPositionWithDominance(lock=multiprocessing.Lock(), isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    reportDate = getterReportDateForRR()
    while datetime.datetime.now() - cv < exitTime:

        # getter Entry list
        eLDf = getterEntryList()
        if len(eLDf) != 0:
            # getting live action flags and they should not be interacted with strategy
            while True:
                try:
                    eTBF, eTSF = getterETLiveActionFlag()
                    break
                except Exception as e:
                    print(f"exception while getting  eTBF, eTSF is {e}")

            # getter entry flags from the belli progressionem
            # ebf, esf = getEntryFlagUsingBasicStrategy()
            # ebf, esf = getEntryFlagUsingTrendingStrategy(cv, isLive)
        else:
            continue

        for index, row in eLDf.iterrows():
            uid = row["id"]
            ot = row["ot"]
            symbol = row['symbol']
            token = row['token']
            if isLive:
                ltp = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token).loc[0, '4']
            else:
                ltp = getLTPFromDistribution(uid, cv)
            lp = row['lp']
            sl = row['sl']
            refTime = row["tOEP"]
            margin = 5
            # condition for long position
            # condition for pre exit
            if ltp == 0 and time.time() - refTime >= 600:
                # row['po'] = 'cancel'
                # row['slo'] = 'cancel'
                getEtAndEntryDropFunction(lock, uid)
            elif ltp == 0:
                continue
            elif ot == "buy":
                if eTBF == "T":
                    getEtAndEntryDropFunction(lock, uid)
                elif ltp >= lp:
                    row['lp'] = ltp
                    # calculation for margin required
                    mr = abs(lp * row["q"] / margin)
                    maDf = getterAvailableMargin()
                    ma = maDf['margin'][0]
                    if mr <= ma:
                        print(f"Entry is place for buy order for {uid} hurray!!!!!!")

                        # assigning pid
                        row['pid'] = getterUpdateAndSetterPositionId(reportDate, lock)

                        row['po'] = 'executed'
                        row['tOP'] = time.time()
                        row['gol'] = 0
                        row['mr'] = mr
                        with lock:
                            # upend the position list
                            getterAppendAndSetterPositionList(row)
                            # remove specific row from Entry list
                            getterDropAndSetterEntryList(uid)
                        # margin debit
                        getterDebitAndSetterAvailableMargin(mr, lock)
                        # fixed portfolio update
                        getterUpdateAndSetterFixedPortfolioWithExpenses(mr, lock)
                        # read and record
                        setPositionDetailsAndCandles(row['pid'], uid, symbol, row, cv, reportDate)
                # elif ltp <= (sl + lp) / 2 or time.time() - refTime >= 1200:
                elif ltp <= sl or time.time() - refTime >= 600:
                    # row['po'] = 'cancel'
                    # row['slo'] = 'cancel'
                    getEtAndEntryDropFunction(lock, uid)

            # condition for short position
            elif ot == "sell":
                if eTSF == "T":
                    getEtAndEntryDropFunction(lock, uid)
                elif ltp <= lp:
                    row['lp'] = ltp
                    # calculation for margin required
                    mr = abs(lp * row["q"] / margin)
                    maDf = getterAvailableMargin()
                    ma = maDf['margin'][0]
                    if mr <= ma:
                        print(f"Entry is place for sell order for {uid} hurray!!!!!!")

                        # assigning position id
                        row['pid'] = getterUpdateAndSetterPositionId(reportDate, lock)

                        row['po'] = 'executed'
                        row['tOP'] = time.time()
                        row['gol'] = 0
                        row['mr'] = mr
                        with lock:
                            # upend the position list
                            getterAppendAndSetterPositionList(row)
                            # remove specific row from Entry list
                            getterDropAndSetterEntryList(uid)
                        # margin debit
                        getterDebitAndSetterAvailableMargin(mr, lock)
                        # fixed portfolio update
                        getterUpdateAndSetterFixedPortfolioWithExpenses(mr, lock)
                        # read and record for position
                        setPositionDetailsAndCandles(row['pid'], uid, symbol, row, cv, reportDate)
                # elif ltp >= (sl + lp) / 2 or time.time() - refTime >= 1200:
                elif ltp >= sl or time.time() - refTime >= 600:
                    # row['po'] = 'cancel'
                    # row['slo'] = 'cancel'
                    getEtAndEntryDropFunction(lock, uid)
        # ctrA = ctrA + 1
        # if ctrA == 10:
        #     print(f"Execution time for getting position list (PL) is {time.time() - startTime}")
        #     ctrA = 0
        # time.sleep(0.125)

# getPosition()
