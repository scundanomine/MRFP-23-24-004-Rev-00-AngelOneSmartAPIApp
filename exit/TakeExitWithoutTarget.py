import datetime
import multiprocessing
import time
import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterReportDateForRR import getterReportDateForRR
from commonudm.GetterTimeDelta import getterTimeDelta
from exit.CheckBearishReversalPatternForExit import checkBearishReversalPatternForExit
from exit.CheckBullishReversalPatternForExit import checkBullishReversalPatternForExit
from exit.ExitUdf import exitUDf
from exit.GetExitInputs import getExitInputs
from exit.GetterUpdateAndSetterExitInputs import getterUpdateAndSetterExitInputs
from ohlcdata.GetFutureLTP import getFutureLTP
from position.GetterPositionList import getterPositionList
from position.GetterUpdateAndSetterPositionList import getterUpdateAndSetterPositionList
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket


def takeExitWithoutTarget(lock=multiprocessing.Lock(), isLive=False):
    startTime = time.time()
    ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    reportDate = getterReportDateForRR()
    while datetime.datetime.now() - cv < exitTime:
        # getter position list
        pLDf = getterPositionList()

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
            ltpP = row["ltpP"]
            if isLive:
                ltp = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token).loc[0, '4']
            else:
                ltp = getFutureLTP(uid)
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
            if (ltp == 0 and time.time() - refTime >= 600) or row['eFlag'] == 1:
                exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                print(f"Exit happened for {uid} boom!!!!!")
                continue
            elif ltp == 0:
                continue
            # exit condition for buy
            elif ot == "buy":
                # condition for sl exit
                if ltp <= sl:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} alas!!!!!")
                    continue
                elif checkBearishReversalPatternForExit(rowCC["berRP"]) and rowC["g"] == 'red' and rowC["C"] <= rowCC["C"]:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                elif rowC["g"] == 'red' and rowCC["g"] == 'red' and rowCCC["g"] == 'red' and rowC["C"] <= rowCC["C"] <= rowCCC["C"]:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                # condition for exit
                elif ltp >= target and time.time() - refTime >= 7200:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} boom!!!!!")
                    continue
            # exit condition for sell
            elif ot == "sell":
                # condition for sl exit
                if ltp >= sl:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for sell order {uid} alas!!!!!")
                    continue
                elif checkBullishReversalPatternForExit(rowCC["bulRP"]) and rowC["g"] == 'green' and rowC["C"] >= rowCC["C"]:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                elif rowC["g"] == 'green' and rowCC["g"] == 'green' and rowCCC["g"] == 'green' and rowC["C"] >= rowCC["C"] >= rowCCC["C"]:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                # condition for exit
                elif ltp <= target or time.time() - refTime >= 7200:
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for sell order {uid} boom!!!!!")
                    continue
            getterUpdateAndSetterPositionList(uid, row, lock)

        ctrA = ctrA + 1
        if ctrA == 50:
            print(f"Execution time for getting Exit Position (EP) is {time.time() - startTime}")
            ctrA = 0
        # time.sleep(0.5)

# takeExit()
