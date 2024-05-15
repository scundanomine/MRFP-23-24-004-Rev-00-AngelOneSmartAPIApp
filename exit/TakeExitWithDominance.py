import datetime
import multiprocessing
import time

import pandas as pd

from belliprogressionem.GetterExitStrategyFlag import getterExitStrategyFlag
from belliprogressionem.belliexit.GetExitFlagUsingTrendingStrategy import getExitFlagUsingTrendingStrategy
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterReportDateForRR import getterReportDateForRR
from commonudm.GetterTimeDelta import getterTimeDelta
from exit.CheckBearishReversalPatternForExit import checkBearishReversalPatternForExit
from exit.CheckBullishReversalPatternForExit import checkBullishReversalPatternForExit
from exit.ExitUdf import exitUDf
from exit.GetExitInputs import getExitInputs
from exit.GetterExitLiveActionFlag import getterExitLiveActionFlag
from exit.GetterUpdateAndSetterExitInputs import getterUpdateAndSetterExitInputs
from ltpdistribution.GetLTPFromDistribution import getLTPFromDistribution
from position.GetterPositionList import getterPositionList
from position.GetterUpdateAndSetterPositionList import getterUpdateAndSetterPositionList
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket


def takeExitWithDominance(lock=multiprocessing.Lock(), isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    reportDate = getterReportDateForRR()
    while datetime.datetime.now() - cv < exitTime:
        # getting live action flags and they should not be interacted with strategy
        while True:
            try:
                eXBLF, eXSLF = getterExitLiveActionFlag()
                break
            except Exception as e:
                print(f"exception while getting  eXBLF, eXSLF is {e}")
                # getter entry flags from the belli progressionem

        # getter position list
        pLDf = getterPositionList()

        # xbf, xsf = getExitFlagUsingBasicStrategy()
        # xbf, xsf = getExitFlagUsingTrendingStrategy(cv, len(pLDf), isLive)

        for index, row in pLDf.iterrows():
            eIDf = getExitInputs()
            token = row['token']
            uid = row["id"]
            symbol = row['symbol']
            pid = row['pid']
            row['rFlag'] = eIDf.loc[uid - 1, 'rFlag']
            row['eFlag'] = eIDf.loc[uid - 1, 'eFlag']
            # getting candle sticks properties
            cdf = getterSpecificCandleData(uid, symbol)
            ot = row["ot"]
            lp = row['lp']
            sl = row['sl']
            target = row['target']
            refTime = row["tOP"]
            q = row['q']
            rowC = cdf.iloc[9]
            rowCC = cdf.iloc[8]
            rowCCC = cdf.iloc[7]
            rsi = rowC['rsi']
            rsiP = rowCC['rsi']
            mr = row['mr']
            # roc = rowC['roc']
            # atr = rowC['atr']
            row["ltpP"] = row["ltp"]
            ltpP = row["ltpP"]
            if isLive:
                ltp = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token).loc[0, '4']
            else:
                ltp = getLTPFromDistribution(uid, cv)
            if ltp != 0:
                row['ltp'] = ltp
                dx = ltp - ltpP
                # calculation for gain or loss why?
                if ot == 'buy':
                    if ltp <= sl:
                        row['gol'] = q * (sl - lp)
                    else:
                        row['gol'] = q * (ltp - lp)
                else:
                    if ltp >= sl:
                        row['gol'] = q * (sl - lp)
                    else:
                        row['gol'] = q * (ltp - lp)
                getterUpdateAndSetterPositionList(uid, row, lock)
            else:
                dx = 0

            # condition for post exit
            if (ltp == 0 and time.time() - refTime >= 7200) or row['eFlag'] == 1:
                row['tOP'] = 'Z'
                exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                print(f"Exit happened for {pid} for {uid} boom!!!!!")
                continue
            elif ltp == 0:
                continue
            # exit condition for buy
            elif ot == "buy":
                # condition for live action exit
                if (eXBLF == 'T') and dx <= 0:
                    row['tOP'] = 'BExDTLiveAndStrFlags'  # Exit due live and strategy flags
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for {pid} for buy order for {uid} emergency!!!!!")
                    continue
                # condition for sl exit
                elif ltp <= sl:
                    row['tOP'] = 'BExDTSLHit'  # exit due to sl hit
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for {pid} for buy order for {uid} alas!!!!!")
                    continue
                elif checkBearishReversalPatternForExit(rowC["berRP"]) and rowC['C'] - ltp >= 0.25 * rowC['atr']:
                    row['po'] = 'doomed!'    # exit due to Bearish reversal pattern
                    row['slo'] = "BDBerRP"
                    getterUpdateAndSetterPositionList(uid, row, lock)
                    continue
                elif rowC["g"] == 'red' and rowCC["g"] == 'red' and rowCCC["g"] == 'red' and rowC["C"] <= rowCC["C"] <= rowCCC["C"]:
                    row['po'] = 'doomed!'    # exit due to continuous red candle
                    row['slo'] = "BDConRedCan"
                    getterUpdateAndSetterPositionList(uid, row, lock)
                    continue
                elif checkBearishReversalPatternForExit(rowCC["berRP"]) and rowCC['C'] - ltp >= 0.25 * rowC['atr']:
                    row['po'] = 'doomed!'
                    row['slo'] = 'BDPreBerRP' # exit due to previous bearish reversal pattern
                    getterUpdateAndSetterPositionList(uid, row, lock)
                    continue
            # exit condition for sell
            elif ot == "sell":
                # condition for live action exit
                if (eXSLF == 'T') and dx >= 0:
                    row['tOP'] = 'SXDTLiveStrFlag'  # exit due to live and strategy flags
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for {pid} for buy order for {uid} alas!!!!!")
                    continue
                # condition for sl exit
                elif ltp >= sl:
                    row['tOP'] = 'SXDTSLHit'  # exit due to sl hit
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for {pid} for sell order {uid} alas!!!!!")
                    continue
                elif checkBullishReversalPatternForExit(rowC["bulRP"]) and ltp - rowC['C'] >= 0.25 * rowC['atr']:
                    row['po'] = 'doomed!'
                    row['slo'] = 'SDBulRP'  # exit due to bullish reversal pattern
                    getterUpdateAndSetterPositionList(uid, row, lock)
                    continue
                elif rowC["g"] == 'green' and rowCC["g"] == 'green' and rowCCC["g"] == 'green' and rowC["C"] >= rowCC["C"] >= rowCCC["C"]:
                    row['po'] = 'doomed!'
                    row['slo'] = 'SDConGreenCan'  # exit due to continuous green candle
                    getterUpdateAndSetterPositionList(uid, row, lock)
                    continue
                elif checkBullishReversalPatternForExit(rowCC["bulRP"]) and ltp - rowCC['C'] >= 0.25 * rowC['atr']:
                    row['po'] = 'doomed!'    # exit due to previous bullish reversal pattern
                    row['slo'] = 'SDPreBulRP'
                    getterUpdateAndSetterPositionList(uid, row, lock)
                    continue

        # ctrA = ctrA + 1
        # if ctrA == 50:
        #     print(f"Execution time for getting Exit Position (EP) is {time.time() - startTime}")
        #     ctrA = 0
        # time.sleep(0.5)

# takeExit()
