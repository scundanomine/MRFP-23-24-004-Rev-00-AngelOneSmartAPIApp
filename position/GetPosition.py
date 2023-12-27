from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterDropAndSetterEntryList import getterDropAndSetterEntryList
from entry.GetterEntryList import getterEntryList
from entry.GetterUpdateAndSetterECBList import getterUpdateAndSetterECBList
from entrytriggeredlist.GetterDropAndSetterEntryTriggeredList import getterDropAndSetterEntryTriggeredList
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET
from margin.GetterAvailableMargin import getterAvailableMargin
from margin.GetterDebitAndSetterAvailableMargin import getterDebitAndSetterAvailableMargin
from ohlcdata.GetFutureLTP import getFutureLTP
from position.GetterAppendAndSetterPositionList import getterAppendAndSetterPositionList
import time
import datetime
import multiprocessing


def getPosition(lock=multiprocessing.Lock()):
    startTime = time.time()
    ctrA = 0
    lock.acquire()
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    lock.release()
    while datetime.datetime.now() - cv < exitTime:
        # getter Entry list
        eLDf = getterEntryList(lock)

        dfItr = eLDf

        for index, row in dfItr.iterrows():
            uid = row["id"]
            ot = row["ot"]
            ltp = getFutureLTP(uid, lock)
            lp = row['lp']
            sl = row['sl']
            refTime = row["tOEP"]
            maDf = getterAvailableMargin()
            ma = maDf['margin'][0]
            mr = row['mr']
            # condition for long position
            # condition for pre exit
            if ltp == 0 and time.time() - refTime >= 1200:
                row['po'] = 'cancel'
                row['slo'] = 'cancel'
                lock.acquire()
                # remove specific row from Entry list
                getterDropAndSetterEntryList(uid)
                # reset of black list
                getterUpdateAndSetterBlackListET(uid, 0)
                getterUpdateAndSetterECBList(uid, False)
                # removal of specific row from ET list
                getterDropAndSetterEntryTriggeredList(uid)
                lock.release()
            elif ltp == 0:
                continue
            elif ot == "buy":
                if ltp >= lp:
                    if mr <= ma:
                        print(f"entry is place for {uid}")
                        row['po'] = 'executed'
                        row['tOP'] = time.time()
                        lock.acquire()
                        # upend the position list
                        getterAppendAndSetterPositionList(row)
                        # remove specific row from Entry list
                        getterDropAndSetterEntryList(uid)
                        # margin debit
                        getterDebitAndSetterAvailableMargin(mr)
                        lock.release()
                # elif ltp <= (sl + lp) / 2 or time.time() - refTime >= 1200:
                elif ltp <= sl or time.time() - refTime >= 1200:
                    row['po'] = 'cancel'
                    row['slo'] = 'cancel'
                    lock.acquire()
                    # remove specific row from Entry list
                    getterDropAndSetterEntryList(uid)
                    # reset of black list
                    getterUpdateAndSetterBlackListET(uid, 0)
                    getterUpdateAndSetterECBList(uid, False)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
                    lock.release()
                else:
                    pass

            # condition for short position
            else:
                if ltp <= lp:
                    if mr <= ma:
                        print(f"entry is place for {uid}")
                        row['po'] = 'executed'
                        row['tOP'] = time.time()
                        lock.acquire()
                        # upend the position list
                        getterAppendAndSetterPositionList(row)
                        # remove specific row from Entry list
                        getterDropAndSetterEntryList(uid)
                        # margin debit
                        getterDebitAndSetterAvailableMargin(mr)
                        lock.release()
                # elif ltp >= (sl + lp) / 2 or time.time() - refTime >= 1200:
                elif ltp >= sl or time.time() - refTime >= 1200:
                    row['po'] = 'cancel'
                    row['slo'] = 'cancel'
                    lock.acquire()
                    # remove specific row from Entry list
                    getterDropAndSetterEntryList(uid)
                    # reset of black list
                    getterUpdateAndSetterBlackListET(uid, 0)
                    getterUpdateAndSetterECBList(uid, False)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
                    lock.release()
                else:
                    pass
        ctrA = ctrA + 1
        print(f"{ctrA} execution time for getting position list (PL) is {time.time() - startTime}")
        time.sleep(0.5)


# getPosition()
