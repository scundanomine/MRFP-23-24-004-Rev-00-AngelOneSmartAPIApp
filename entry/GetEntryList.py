from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterECBList import getterECBList
from entry.GetterEntryList import getterEntryList
from entry.LongPositionCalculator import longPositionCalculator
from entry.ShortPositionCalculator import shortPositionCalculator
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
import datetime
from margin.GetterAvailableMargin import getterAvailableMargin
from margin.SetterAvailableMargin import setterAvailableMargin
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
        # Getter for entry list
        eLDf = getterEntryList(lock)

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
            ltp = getFutureLTP(uid, ot, lock)
            if eCBLDf['eCBFlag'][uid-1] or ltp == 0:
                continue
            else:
                if ot == 'buy':
                    q, sl, target = longPositionCalculator(ltp, atr, 500, 1.2, 50000, margin, 1.5)
                else:
                    q, sl, target = shortPositionCalculator(ltp, atr, 500, 1.2, 50000, margin, 1.5)
                # calculation for margin required
                mr = abs(1.01*ltp*q/margin)
                maDf = getterAvailableMargin()
                ma = maDf['margin'][0]
                if mr <= ma:
                    upList = [uid, sector, symbol, token, ot, ltp, 1.01*ltp, q, sl, target, mr, 'open', 'open', '', datetime.datetime.now()]
                    eLDf.loc[len(eLDf)] = upList
                    eCBLDf['eCBFlag'][uid - 1] = True
                    maDf.loc[0, 'margin'] = ma - mr
                    setterAvailableMargin(maDf)
                else:
                    pass
        lock.acquire()
        # setter for getter Entry calculated and entry happened black list
        eCBLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv", index=False)

        # setter for Entry list
        eLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\EntryList.csv", index=False)
        lock.release()
        ctrA = ctrA + 1
        print(f"{ctrA} execution time for getting entry triggered list is {time.time() - startTime}")
        time.sleep(5)
