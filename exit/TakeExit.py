import time
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterReportDateForRR import getterReportDateForRR
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterUpdateAndSetterECBList import getterUpdateAndSetterECBList
from entrytriggeredlist.GetterDropAndSetterEntryTriggeredList import getterDropAndSetterEntryTriggeredList
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET
from exit.GetExitInputs import getExitInputs
from exit.GetterUpdateAndSetterExitInputs import getterUpdateAndSetterExitInputs
from margin.GetterCreditAndSetterAvailableMargin import getterCreditAndSetterAvailableMargin
from ohlcdata.GetFutureLTP import getFutureLTP
from portfolio.GetterUpdateAndSetterFixedPortfolio import getterUpdateAndSetterFixedPortfolio
from position.GetterDropAndSetterPositionList import getterDropAndSetterPositionList
from position.GetterPositionList import getterPositionList
from position.GetterUpdateAndSetterPositionList import getterUpdateAndSetterPositionList
import datetime
import multiprocessing
from readandrecord.SetExitDetailsAndCandles import setExitDetailsAndCandles
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket
import pandas as pd


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
            ltpP = row["ltpP"]
            if isLive:
                ltp = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token).loc[0, '4']
            else:
                ltp = getFutureLTP(uid)
            if ltp != 0:
                row['ltp'] = ltp
                dx = ltp - ltpP
                # calculation for gain or loss why?
                row['gol'] = q * (ltp - lp)
                getterUpdateAndSetterPositionList(uid, row, lock)
            else:
                dx = 0

            # condition for post exit
            if (ltp == 0 and time.time() - refTime >= 600) or row['eFlag'] == 1:
                with lock:
                    # remove specific row from Entry list
                    getterDropAndSetterPositionList(uid)
                    # reset of black list
                    getterUpdateAndSetterBlackListET(uid, 0)
                    getterUpdateAndSetterECBList(uid, 0)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
                getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                getterCreditAndSetterAvailableMargin(mr, lock)
                getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                # read and record for exit
                setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate)
                print(f"Exit happened for {uid} boom!!!!!")
                continue
            elif ltp == 0:
                continue
            # exit condition for buy
            elif ot == "buy":
                # condition for sl exit
                if ltp <= sl:
                    with lock:
                        # remove specific row from Entry list
                        getterDropAndSetterPositionList(uid)
                        # reset of black list
                        getterUpdateAndSetterBlackListET(uid, 0)
                        getterUpdateAndSetterECBList(uid, 0)
                        # removal of specific row from ET list
                        getterDropAndSetterEntryTriggeredList(uid)
                    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                    getterCreditAndSetterAvailableMargin(mr, lock)
                    getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                    # read and record for exit
                    setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate)
                    print(f"Exit happened for buy order for {uid} alas!!!!!")
                    continue
                # condition for Trailing stop loss
                elif row["rFlag"] == 1:
                    if dx > 0:
                        row['sl'] = sl + dx
                        row['target'] = target + dx
                    elif ltp <= lp + 0.7*(target-lp) or (rowC < rowCC < rowCCC):
                        row['eFlag'] = 1
                        row['rFlag'] = 0
                        getterUpdateAndSetterExitInputs([uid, 0, 1], lock)
                # condition for exit
                elif ltp >= target or ltp <= sl or time.time() - refTime >= 1200:
                    with lock:
                        # remove specific row from Entry list
                        getterDropAndSetterPositionList(uid)
                        # reset of black list
                        getterUpdateAndSetterBlackListET(uid, 0)
                        getterUpdateAndSetterECBList(uid, 0)
                        # removal of specific row from ET list
                        getterDropAndSetterEntryTriggeredList(uid)
                    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                    getterCreditAndSetterAvailableMargin(mr, lock)
                    getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                    # read and record for exit
                    setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate)
                    print(f"Exit happened for buy order for {uid} boom!!!!!")
                    continue
                # condition for riding
                elif ltp - lp >= 0.8 * (target - lp) and (rsi >= 70 and rsi >= rsiP):
                    row['sl'] = sl + dx
                    row['target'] = target + dx
                    row['rFlag'] = 1
                    getterUpdateAndSetterExitInputs([uid, 1, 0], lock)
            # exit condition for sell
            elif ot == "sell":
                # condition for sl exit
                if ltp >= sl:
                    with lock:
                        # remove specific row from Entry list
                        getterDropAndSetterPositionList(uid)
                        # reset of black list
                        getterUpdateAndSetterBlackListET(uid, 0)
                        getterUpdateAndSetterECBList(uid, 0)
                        # removal of specific row from ET list
                        getterDropAndSetterEntryTriggeredList(uid)
                    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                    getterCreditAndSetterAvailableMargin(mr, lock)
                    getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                    # read and record for exit
                    setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate)
                    print(f"Exit happened for sell order {uid} alas!!!!!")
                    continue
                # condition for Trailing stop loss
                elif row["rFlag"] == 1:
                    if dx < 0:
                        row['sl'] = sl + dx
                        row['target'] = target + dx
                    elif ltp >= lp - 0.7*(lp-target) or (rowC > rowCC > rowCCC):
                        row['eFlag'] = 1
                        row['rFlag'] = 0
                        getterUpdateAndSetterExitInputs([uid, 0, 1], lock)
                # condition for exit
                elif ltp <= target or ltp >= sl or time.time() - refTime >= 1200:
                    with lock:
                        # remove specific row from Entry list
                        getterDropAndSetterPositionList(uid)
                        # reset of black list
                        getterUpdateAndSetterBlackListET(uid, 0)
                        getterUpdateAndSetterECBList(uid, 0)
                        # removal of specific row from ET list
                        getterDropAndSetterEntryTriggeredList(uid)
                    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                    getterCreditAndSetterAvailableMargin(mr, lock)
                    getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                    # read and record for exit
                    setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate)
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
