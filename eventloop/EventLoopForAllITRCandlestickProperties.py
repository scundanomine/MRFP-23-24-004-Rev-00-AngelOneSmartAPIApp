import datetime
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
import time
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from eventloop.GetAllItrCandlesticksProperties import getAllItrCandlesticksProperties
from ohlcdata.GetterPDS import getterPDS
import multiprocessing


def eventLoopForAllITRCandlestickProperties(lock=multiprocessing.Lock()):
    startTime = time.time()
    lock.acquire()
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    lock.release()
    while datetime.datetime.now() - cv < exitTime:
        # get the id and symbol df
        lock.acquire()
        gDf = getterRequiredSymbolAndTokenList()

        # getter past candle data
        pDs = getterPDS()
        lock.release()
        lPDs = pDs.values.tolist()

        # iterate gDf
        for index, row in gDf.iterrows():
            uid = row['id']
            symbol = row['symbol']
            lock.acquire()
            psTime = getterSpecificCandleData(uid, symbol).loc[9, 'time']
            lock.release()
            data = lPDs[uid - 1]
            fsTime = data[0]
            if psTime == fsTime:
                continue
            else:
                # calculation for candle properties
                getAllItrCandlesticksProperties(uid, symbol, data, lock)
        print(f"Execution time for All Itr candle properties (CP) is {time.time() - startTime}")
        time.sleep(5)


# eventLoopForAllITRCandlestickProperties()
