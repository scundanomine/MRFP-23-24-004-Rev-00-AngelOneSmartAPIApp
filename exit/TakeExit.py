import time
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterUpdateAndSetterECBList import getterUpdateAndSetterECBList
from entrytriggeredlist.GetterDropAndSetterEntryTriggeredList import getterDropAndSetterEntryTriggeredList
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET
from ohlcdata.GetFutureLTP import getFutureLTP
from portfolio.GetterPortfolio import getterPortfolio
from portfolio.SetterPortfolio import setterPortfolio
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

        # getter portfolio
        pfDf = getterPortfolio()

        dfItr = pLDf

        for index, row in dfItr.iterrows():
            uid = row["id"]
            symbol = row['symbol']
            # getting candle sticks properties
            cdf = getterSpecificCandleData(uid, symbol, lock)
            ot = row["ot"]
            ltp = getFutureLTP(uid, ot, lock)
            lp = row['lp']
            sl = row['sl']
            target = row['target']
            refTime = row["tOP"]
            q = row['q']
            rowC = cdf.iloc[9]
            rowCC = cdf.iloc[8]
            rsi = rowC['rsi']
            rsiP = rowCC['rsi']
            # roc = rowC['roc']
            # atr = rowC['atr']
            ltpP = row["ltpP"]
            dx = ltp - ltpP
            # calculation for gain or loss why?
            row['gol'] = q * (ltp - lp)

            # calculation for portfolio
            pfDf.loc[0, 'portfolio'] = pfDf["portfolio"][0] + q * (ltp - lp)

            # setter for portfolio
            setterPortfolio(pfDf)
            # condition for post exit
            if ltp == 0 and time.time() - refTime >= 1800:
                lock.acquire()
                # remove specific row from Entry list
                getterDropAndSetterPositionList(uid)
                # reset of black list
                getterUpdateAndSetterBlackListET(uid, 0)
                getterUpdateAndSetterECBList(uid, False)
                # removal of specific row from ET list
                getterDropAndSetterEntryTriggeredList(uid)
                lock.release()
            elif ltp == 0:
                continue
            # exit condition for buy
            if ot == "buy":
                # condition for Trailing stop loss
                if row["rFlag"]:
                    if dx > 0:
                        row['sl'] = sl + dx
                        row['target'] = target + dx
                    elif ltp >= target or (rsi <= 50 and rsi <= rsiP):
                        row['eFlag'] = True
                        row['rFlag'] = False
                # condition for exit
                elif ltp >= target or time.time() - refTime >= 1800 or row['eFlag']:
                    lock.acquire()
                    # remove specific row from Entry list
                    getterDropAndSetterPositionList(uid)
                    # reset of black list
                    getterUpdateAndSetterBlackListET(uid, 0)
                    getterUpdateAndSetterECBList(uid, False)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
                    lock.release()
                # condition for riding
                elif ltp - lp >= 0.8 * (target - lp) and (rsi >= 70 and rsi >= rsiP):
                    row['sl'] = sl + dx
                    row['target'] = target + dx
                    row['rFlag'] = False
            # exit condition for sell
            else:
                # condition for Trailing stop loss
                if row["rFlag"]:
                    if dx < 0:
                        row['sl'] = sl - dx
                        row['target'] = target - dx
                    elif ltp <= target or (rsi >= 50 and rsi >= rsiP):
                        row['eFlag'] = True
                        row['rFlag'] = False
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
                # condition for riding
                elif ltp - lp <= 0.8 * (target - lp) and (rsi <= 30 and rsi <= rsiP):
                    row['sl'] = sl - dx
                    row['target'] = target - dx
                    row['rFlag'] = False
            lock.acquire()
            getterUpdateAndSetterPositionList(uid, row)
            lock.release()

        ctrA = ctrA + 1
        print(f"{ctrA} execution time for getting Exit Position is {time.time() - startTime}")
        time.sleep(0.5)
