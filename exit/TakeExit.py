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


def takeExit(lock=multiprocessing.Lock(), isLive=False):
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
            row["ltpP"] = row["ltp"]
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
            if (ltp == 0 and time.time() - refTime >= 7200) or row['eFlag'] == 1:
                row['tOP'] = 'Z'
                exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                print(f"Exit happened for {uid} boom!!!!!")
                continue
            elif ltp == 0:
                continue
            # exit condition for buy
            elif ot == "buy":
                # condition for sl exit
                if ltp <= sl:
                    row['tOP'] = 'a'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} alas!!!!!")
                    continue
                # elif rowC['C'] - ltp >= 1.5 * rowC['atr']:
                #     row['tOP'] = 'b'
                #     exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                #     print(f"Exit happened for buy order for {uid} wow!!!!!")
                #     continue
                # elif rowC["g"] == 'red' and rowCC["g"] == 'red' and (rowC['s'] + rowCC['s']) >= 2:
                #     row['tOP'] = 'c'
                #     exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                #     print(f"Exit happened for buy order for {uid} wow!!!!!")
                #     continue
                elif checkBearishReversalPatternForExit(rowC["berRP"]) and rowC['C'] - ltp >= 0.25 * rowC['atr']:
                    row['tOP'] = 'd'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                elif rowC["g"] == 'red' and rowCC["g"] == 'red' and rowCCC["g"] == 'red' and rowC["C"] <= rowCC["C"] <= rowCCC["C"]:
                    row['tOP'] = 'e'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                # condition for Trailing stop loss
                elif row["rFlag"] == 1:
                    if dx > 0:
                        row['sl'] = sl + dx
                        row['target'] = target + dx
                        getterUpdateAndSetterPositionList(uid, row, lock)
                    elif ltp <= lp + 0.5 * (target - lp):
                        row['eFlag'] = 1
                        row['rFlag'] = 0
                        getterUpdateAndSetterExitInputs([uid, 0, 1], lock)
                        getterUpdateAndSetterPositionList(uid, row, lock)
                # condition for exit
                elif ltp >= target or time.time() - refTime >= 7200:
                    row['tOP'] = 'f'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} boom!!!!!")
                    continue
                # condition for riding
                elif ltp - lp >= 0.8 * (target - lp) and (rsi >= 70 and rsi >= rsiP):
                    row['sl'] = sl + dx
                    row['target'] = target + dx
                    row['rFlag'] = 1
                    getterUpdateAndSetterExitInputs([uid, 1, 0], lock)
                    getterUpdateAndSetterPositionList(uid, row, lock)
            # exit condition for sell
            elif ot == "sell":
                # condition for sl exit
                if ltp >= sl:
                    row['tOP'] = 'A'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for sell order {uid} alas!!!!!")
                    continue
                # elif ltp - rowC['C'] >= 1.5 * rowC['atr']:
                #     row['tOP'] = 'B'
                #     exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                #     print(f"Exit happened for sell order for {uid} wow!!!!!")
                #     continue
                # elif rowC["g"] == 'green' and rowCC["g"] == 'green' and (rowC['s'] + rowCC['s']) >= 2:
                #     row['tOP'] = 'C'
                #     exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                #     print(f"Exit happened for buy order for {uid} wow!!!!!")
                #     continue
                elif checkBullishReversalPatternForExit(rowC["bulRP"]) and ltp - rowC['C'] >= 0.25 * rowC['atr']:
                    row['tOP'] = 'D'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                elif rowC["g"] == 'green' and rowCC["g"] == 'green' and rowCCC["g"] == 'green' and rowC["C"] >= rowCC["C"] >= rowCCC["C"]:
                    row['tOP'] = 'E'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} wow!!!!!")
                    continue
                # condition for Trailing stop loss
                elif row["rFlag"] == 1:
                    if dx < 0:
                        row['sl'] = sl + dx
                        row['target'] = target + dx
                        getterUpdateAndSetterPositionList(uid, row, lock)
                    elif ltp >= lp - 0.5 * (lp - target):
                        row['eFlag'] = 1
                        row['rFlag'] = 0
                        getterUpdateAndSetterExitInputs([uid, 0, 1], lock)
                        getterUpdateAndSetterPositionList(uid, row, lock)
                # condition for exit
                elif ltp <= target or time.time() - refTime >= 7200:
                    row['tOP'] = 'F'
                    exitUDf(pid, uid, symbol, row, cv, reportDate, mr, row['gol'], lock)
                    print(f"Exit happened for sell order {uid} boom!!!!!")
                    continue
                # condition for riding
                elif ltp - lp <= 0.8 * (target - lp) and (rsi <= 30 and rsi <= rsiP):
                    row['sl'] = sl - dx
                    row['target'] = target - dx
                    row['rFlag'] = 1
                    getterUpdateAndSetterExitInputs([uid, 1, 0], lock)
                    getterUpdateAndSetterPositionList(uid, row, lock)

        ctrA = ctrA + 1
        if ctrA == 50:
            print(f"Execution time for getting Exit Position (EP) is {time.time() - startTime}")
            ctrA = 0
        # time.sleep(0.5)

# takeExit()
