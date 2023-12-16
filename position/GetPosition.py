from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entry.GetterECBList import getterECBList
from entry.GetterEntryList import getterEntryList
from entry.SetterECBList import setterECBList
from entry.SetterEntryList import setterEntryList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
from entrytriggeredlist.SetterBlackListET import setterBlackListET
from entrytriggeredlist.SetterEntryTriggeredList import setterEntryTriggeredList
from ohlcdata.GetFutureLTP import getFutureLTP
from position.GetterPositionList import getterPositionList
from position.SetterPositionList import setterPositionList
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
        # getter ET list
        eTDf = getterEntryTriggeredList(lock)

        # getter ET black list
        eTBDf = getterBlackListET(lock)

        # getter Entry list
        eLDf = getterEntryList(lock)

        # getter Entry calculation black list
        eCBDf = getterECBList(lock)

        # getter position list
        pLDf = getterPositionList(lock)

        dfItr = eLDf

        for index, row in dfItr.iterrows():
            uid = row["id"]
            ot = row["ot"]
            ltp = getFutureLTP(uid, ot, lock)
            lo = row['lo']
            sl = row['sl']
            refTime = row["tOEP"]
            i = eTDf[(eTDf.id == uid)].index
            # condition for long position
            if ot is "buy":
                if ltp >= lo:
                    print(f"entry is place for {uid}")
                    row['po'] = 'executed'
                    row['tOP'] = time.time()
                    # upend the list
                    pLDf.iLoc[len(pLDf)] = row
                    # remove specific row from Entry list
                    eLDf.drop(index)
                elif ltp <= (sl + lo) / 2 or time.time() - refTime >= 600:
                    row['po'] = 'cancel'
                    row['sl'] = 'cancel'
                    # remove specific row from Entry list
                    eLDf.drop(index)
                    # reset of black list
                    eTBDf.loc[uid-1, "bFlag"] = False
                    eCBDf.loc[uid-1, "bELFlag"] = False
                    # removal of specific row from ET list
                    eTDf.drop(i)
                else:
                    pass

            # condition for short position
            else:
                if ltp <= lo:
                    print(f"entry is place for {uid}")
                    row['po'] = 'executed'
                    row['tOP'] = time.time()
                    # upend the list
                    pLDf.iLoc[len(pLDf)] = row
                    # remove specific row from Entry list
                    eLDf.drop(index)
                elif ltp >= (sl + lo) / 2 or time.time() - refTime >= 600:
                    row['po'] = 'cancel'
                    row['sl'] = 'cancel'
                    # remove specific row from Entry list
                    eLDf.drop(index)
                    # reset of black list
                    eTBDf.loc[uid-1, "bFlag"] = False
                    eCBDf.loc[uid-1, "bELFlag"] = False
                    # removal of specific row from ET list
                    eTDf.drop(i)
                else:
                    pass

        # setter for eTDf
        setterEntryTriggeredList(eTDf, lock)

        # setter for eTBDf
        setterBlackListET(eTBDf, lock)

        # setter for eLDf
        setterEntryList(eLDf, lock)

        # setter for eCBDf
        setterECBList(eCBDf, lock)

        # setter for pLDf
        setterPositionList(pLDf, lock)
        ctrA = ctrA + 1
        print(f"{ctrA} execution time for getting position list is {time.time() - startTime}")
        time.sleep(0.5)
