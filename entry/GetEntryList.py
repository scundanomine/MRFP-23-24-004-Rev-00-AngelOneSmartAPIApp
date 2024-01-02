from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterAppendAndSetterEntryList import getterAppendAndSetterEntryList
from entry.GetterECBList import getterECBList
from entry.GetterUpdateAndSetterECBList import getterUpdateAndSetterECBList
from entry.LongPositionCalculator import longPositionCalculator
from entry.ShortPositionCalculator import shortPositionCalculator
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
import datetime
import time
import multiprocessing
from ohlcdata.GetFutureLTP import getFutureLTP


def getEntryList(lock=multiprocessing.Lock()):
    startTime = time.time()
    ctrA = 0
    lock.acquire()
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    lock.release()
    while datetime.datetime.now() - cv < exitTime:
        # getter Entry calculated and entry happened black list
        eCBLDf = getterECBList(lock)

        # getter ET list
        eTDf = getterEntryTriggeredList(lock)

        for index, row in eTDf.iterrows():
            uid = row['id']
            sector = row['sector']
            symbol = row['symbol']
            token = row['token']
            atr = row['atr']
            margin = 5
            ot = row['ot']
            ltp = getFutureLTP(uid, lock)
            if eCBLDf.loc[uid - 1, 'eCBFlag'] or ltp == 0:
                continue
            else:
                if ot == 'buy':
                    q, sl, target = longPositionCalculator(ltp, atr, 500, 1.2, 50000, margin, 1.5)
                    lp = 1.00025 * ltp
                else:
                    q, sl, target = shortPositionCalculator(ltp, atr, 500, 1.2, 50000, margin, 1.5)
                    lp = 0.99975 * ltp

                # calculation for margin required
                mr = abs(lp * q / margin)

                upList = [uid, sector, symbol, token, ot, ltp, lp, q, sl, target, mr, 'open', 'open', '', 0,
                          time.time(), '', '', ltp, False, False]
                lock.acquire()
                getterAppendAndSetterEntryList(upList)
                getterUpdateAndSetterECBList(uid, True)
                lock.release()
        ctrA = ctrA + 1
        print(f"{ctrA} execution time for getting Entry List (EL) is {time.time() - startTime}")
        time.sleep(5)


# getEntryList()
