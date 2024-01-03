import time
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
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


def takeExit(lock=multiprocessing.Lock()):
    startTime = time.time()
    ctrA = 0
    lock.acquire()
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    lock.release()
    while datetime.datetime.now() - cv < exitTime:
        # getter position list
        pLDf = getterPositionList(lock)

        dfItr = pLDf

        eIDf = getExitInputs(lock)

        for index, row in dfItr.iterrows():
            uid = row["id"]
            symbol = row['symbol']
            row['rFlag'] = eIDf.loc[uid - 1, 'rFlag']
            row['eFlag'] = eIDf.loc[uid - 1, 'eFlag']
            # getting candle sticks properties
            cdf = getterSpecificCandleData(uid, symbol, lock)
            ot = row["ot"]
            lp = row['lp']
            sl = row['sl']
            target = row['target']
            refTime = row["tOP"]
            q = row['q']
            rowC = cdf.iloc[9]
            rowCC = cdf.iloc[8]
            rsi = rowC['rsi']
            rsiP = rowCC['rsi']
            mr = row['mr']
            # roc = rowC['roc']
            # atr = rowC['atr']
            ltpP = row["ltpP"]
            ltp = getFutureLTP(uid, lock)
            if ltp != 0:
                row['ltp'] = ltp
                dx = ltp - ltpP
                # calculation for gain or loss why?
                row['gol'] = q * (ltp - lp)
                getterUpdateAndSetterPositionList(uid, row, lock)
            else:
                dx = 0

            # condition for post exit
            if (ltp == 0 and time.time() - refTime >= 1800) or row['eFlag'] == 1:
                lock.acquire()
                # remove specific row from Entry list
                getterDropAndSetterPositionList(uid)
                # reset of black list
                getterUpdateAndSetterBlackListET(uid, 0)
                getterUpdateAndSetterECBList(uid, False)
                # removal of specific row from ET list
                getterDropAndSetterEntryTriggeredList(uid)
                lock.release()
                getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                getterCreditAndSetterAvailableMargin(mr, lock)
                getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                print(f"Exit happened for {uid} boom!!!!!")
                continue
            elif ltp == 0:
                continue
            # exit condition for buy
            elif ot == "buy":
                # condition for Trailing stop loss
                if row["rFlag"] == 1:
                    if dx > 0:
                        row['sl'] = sl + dx
                        row['target'] = target + dx
                    elif ltp >= target or (rsi <= 50 and rsi <= rsiP):
                        row['eFlag'] = 1
                        row['rFlag'] = 0
                # condition for exit
                elif ltp >= target or time.time() - refTime >= 1800 or row['eFlag'] == 1:
                    lock.acquire()
                    # remove specific row from Entry list
                    getterDropAndSetterPositionList(uid)
                    # reset of black list
                    getterUpdateAndSetterBlackListET(uid, 0)
                    getterUpdateAndSetterECBList(uid, False)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
                    lock.release()
                    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                    getterCreditAndSetterAvailableMargin(mr, lock)
                    getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                    print(f"Exit happened for buy order for {uid} boom!!!!!")
                    continue
                # condition for riding
                elif ltp - lp >= 0.8 * (target - lp) and (rsi >= 70 and rsi >= rsiP):
                    row['sl'] = sl + dx
                    row['target'] = target + dx
                    row['rFlag'] = 1
                    getterUpdateAndSetterExitInputs([uid, 1, 0], lock)
            # exit condition for sell
            else:
                # condition for Trailing stop loss
                if row["rFlag"] == 1:
                    if dx < 0:
                        row['sl'] = sl - dx
                        row['target'] = target - dx
                    elif ltp <= target or (rsi >= 50 and rsi >= rsiP):
                        row['eFlag'] = 1
                        row['rFlag'] = 0
                        getterUpdateAndSetterExitInputs([uid, 0, 1], lock)
                # condition for exit
                elif ltp <= target or time.time() - refTime >= 1800 or row['eFlag']:
                    lock.acquire()
                    # remove specific row from Entry list
                    getterDropAndSetterPositionList(uid)
                    # reset of black list
                    getterUpdateAndSetterBlackListET(uid, 0)
                    getterUpdateAndSetterECBList(uid, False)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
                    lock.release()
                    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
                    getterCreditAndSetterAvailableMargin(mr, lock)
                    getterUpdateAndSetterFixedPortfolio(row['gol'], lock)
                    print(f"Exit happened for sell order {uid} boom!!!!!")
                    continue
                # condition for riding
                elif ltp - lp <= 0.8 * (target - lp) and (rsi <= 30 and rsi <= rsiP):
                    row['sl'] = sl - dx
                    row['target'] = target - dx
                    row['rFlag'] = 0
                    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
            getterUpdateAndSetterPositionList(uid, row, lock)

        ctrA = ctrA + 1
        if ctrA == 100:
            print(f"{ctrA} execution time for getting Exit Position (EP) is {time.time() - startTime}")
            ctrA = 0
        # time.sleep(0.5)


# takeExit()
