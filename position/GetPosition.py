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
from position.GetterUpdateAndSetterPositionId import getterUpdateAndSetterPositionId
from readandrecord.SetPositionDetailsAndCandles import setPositionDetailsAndCandles
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket
import pandas as pd


def getPosition(lock=multiprocessing.Lock(), isLive=False):
    startTime = time.time()
    ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # getter Entry list
        eLDf = getterEntryList()

        for index, row in eLDf.iterrows():
            uid = row["id"]
            ot = row["ot"]
            symbol = row['symbol']
            token = row['token']
            if isLive:
                ltp = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token).loc[0, '4']
            else:
                ltp = getFutureLTP(uid)
            lp = row['lp']
            sl = row['sl']
            refTime = row["tOEP"]
            mr = row['mr']
            # condition for long position
            # condition for pre exit
            if ltp == 0 and time.time() - refTime >= 600:
                # row['po'] = 'cancel'
                # row['slo'] = 'cancel'
                with lock:
                    # remove specific row from Entry list
                    getterDropAndSetterEntryList(uid)
                    # reset of black list
                    getterUpdateAndSetterBlackListET(uid, 0)
                    getterUpdateAndSetterECBList(uid, 0)
                    # removal of specific row from ET list
                    getterDropAndSetterEntryTriggeredList(uid)
            elif ltp == 0:
                continue
            elif ot == "buy":
                if ltp >= lp:
                    maDf = getterAvailableMargin()
                    ma = maDf['margin'][0]
                    if mr <= ma:
                        print(f"Entry is place for buy order for {uid} hurray!!!!!!")

                        # assigning pid
                        row['pid'] = getterUpdateAndSetterPositionId(lock)

                        row['po'] = 'executed'
                        row['tOP'] = time.time()
                        row['gol'] = 0
                        with lock:
                            # upend the position list
                            getterAppendAndSetterPositionList(row)
                            # remove specific row from Entry list
                            getterDropAndSetterEntryList(uid)
                        # margin debit
                        getterDebitAndSetterAvailableMargin(mr, lock)
                        # read and record
                        setPositionDetailsAndCandles(row['pid'], uid, symbol, row, cv)
                # elif ltp <= (sl + lp) / 2 or time.time() - refTime >= 1200:
                elif ltp <= sl or time.time() - refTime >= 600:
                    # row['po'] = 'cancel'
                    # row['slo'] = 'cancel'
                    with lock:
                        # remove specific row from Entry list
                        getterDropAndSetterEntryList(uid)
                        # reset of black list
                        getterUpdateAndSetterBlackListET(uid, 0)
                        getterUpdateAndSetterECBList(uid, 0)
                        # removal of specific row from ET list
                        getterDropAndSetterEntryTriggeredList(uid)

            # condition for short position
            elif ot == "sell":
                if ltp <= lp:
                    maDf = getterAvailableMargin()
                    ma = maDf['margin'][0]
                    if mr <= ma:
                        print(f"Entry is place for sell order for {uid} hurray!!!!!!")

                        # assigning position id
                        row['pid'] = getterUpdateAndSetterPositionId(lock)

                        row['po'] = 'executed'
                        row['tOP'] = time.time()
                        row['gol'] = 0
                        with lock:
                            # upend the position list
                            getterAppendAndSetterPositionList(row)
                            # remove specific row from Entry list
                            getterDropAndSetterEntryList(uid)
                        # margin debit
                        getterDebitAndSetterAvailableMargin(mr, lock)
                        # read and record for position
                        setPositionDetailsAndCandles(row['pid'], uid, symbol, row, cv)
                # elif ltp >= (sl + lp) / 2 or time.time() - refTime >= 1200:
                elif ltp >= sl or time.time() - refTime >= 600:
                    # row['po'] = 'cancel'
                    # row['slo'] = 'cancel'
                    with lock:
                        # remove specific row from Entry list
                        getterDropAndSetterEntryList(uid)
                        # reset of black list
                        getterUpdateAndSetterBlackListET(uid, 0)
                        getterUpdateAndSetterECBList(uid, 0)
                        # removal of specific row from ET list
                        getterDropAndSetterEntryTriggeredList(uid)
        ctrA = ctrA + 1
        if ctrA == 10:
            print(f"Execution time for getting position list (PL) is {time.time() - startTime}")
            ctrA = 0
        time.sleep(1)


# getPosition()
