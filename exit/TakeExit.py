import time
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterECBList import getterECBList
from entry.SetterECBList import setterECBList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
from entrytriggeredlist.SetterBlackListET import setterBlackListET
from entrytriggeredlist.SetterEntryTriggeredList import setterEntryTriggeredList
from ohlcdata.GetFutureLTP import getFutureLTP
from portfolio.GetterPortfolio import getterPortfolio
from portfolio.SetterPortfolio import setterPortfolio
from position.GetterPositionList import getterPositionList
from position.SetterPositionList import setterPositionList
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
        # getter ET list
        eTDf = getterEntryTriggeredList(lock)

        # getter ET black list
        eTBDf = getterBlackListET(lock)

        # getter Entry calculation black list
        eCBDf = getterECBList(lock)

        # getter position list
        pLDf = getterPositionList(lock)

        # getter portfolio
        pfDf = getterPortfolio()

        dfItr = pLDf

        for index, row in dfItr.iterrows():
            uid = row["id"]
            ot = row["ot"]
            ltp = getFutureLTP(uid, ot, lock)
            lo = row['lo']
            sl = row['sl']
            target = row['target']
            refTime = row["tOP"]
            q = row['q']
            rowC = eTDf.loc[(eTDf['id'] == uid)]
            rsi = rowC['rsi0']
            rsiP = rowC['rsi1']
            roc = rowC['roc0']
            atr = rowC['atr']
            ltpP = row["ltpP"]
            i = eTDf[(eTDf.id == uid)].index
            dx = ltp - ltpP
            # calculation for gain or loss
            pLDf.loc[index, 'gol'] = q * (ltp - lo)

            # calculation for portfolio
            pfDf.loc[0, 'portfolio'] = pfDf["portfolio"][0] + q * (ltp - lo)

            # setter for portfolio
            setterPortfolio(pfDf)

            # exit condition for buy
            if ot is "buy":
                # condition for Trailing stop loss
                if row["rFlag"]:
                    if dx > 0:
                        pLDf.loc[index, 'sl'] = sl + dx
                        pLDf.loc[index, 'target'] = target + dx
                    elif ltp >= target or (rsi <= 50 and rsi <= rsiP):
                        pLDf.loc[index, 'eFlag'] = True
                        pLDf.loc[index, 'rFlag'] = False
                # condition for exit
                elif ltp >= target or time.time() - refTime >= 1800 or row['eFlag']:
                    eTDf.drop(i)
                    pLDf.drop(index)
                    eTBDf.loc[uid - 1, "bFlag"] = False
                    eCBDf.loc[uid - 1, "bELFlag"] = False
                # condition for riding
                elif ltp - lo >= 0.8 * (target - lo) and (rsi >= 70 and rsi >= rsiP):
                    pLDf.loc[index, 'sl'] = sl + dx
                    pLDf.loc[index, 'target'] = target + dx
                    pLDf.loc[index, 'rFlag'] = False
            # exit condition for sell
            else:
                # condition for Trailing stop loss
                if row["rFlag"]:
                    if dx < 0:
                        pLDf.loc[index, 'sl'] = sl - dx
                        pLDf.loc[index, 'target'] = target - dx
                    elif ltp <= target or (rsi >= 50 and rsi >= rsiP):
                        pLDf.loc[index, 'eFlag'] = True
                        pLDf.loc[index, 'rFlag'] = False
                # condition for exit
                elif ltp <= target or time.time() - refTime >= 1800 or row['eFlag']:
                    eTDf.drop(i)
                    pLDf.drop(index)
                    eTBDf.loc[uid - 1, "bFlag"] = False
                    eCBDf.loc[uid - 1, "bELFlag"] = False
                # condition for riding
                elif ltp - lo <= 0.8 * (target - lo) and (rsi <= 30 and rsi <= rsiP):
                    pLDf.loc[index, 'sl'] = sl - dx
                    pLDf.loc[index, 'target'] = target - dx
                    pLDf.loc[index, 'rFlag'] = False

            # setter for eTDf
            setterEntryTriggeredList(eTDf, lock)

            # setter for eTBDf
            setterBlackListET(eTBDf, lock)

            # setter for eCBDf
            setterECBList(eCBDf, lock)

            # setter for pLDf
            setterPositionList(pLDf, lock)
            ctrA = ctrA + 1
            print(f"{ctrA} execution time for getting exit is {time.time() - startTime}")
            time.sleep(0.5)
