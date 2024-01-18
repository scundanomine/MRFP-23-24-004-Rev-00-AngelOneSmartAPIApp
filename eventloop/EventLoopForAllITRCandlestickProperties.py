import datetime
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
import time
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from eventloop.GetAllItrCandlesticksProperties import getAllItrCandlesticksProperties
from ohlcdata.GetterPDS import getterPDS
import multiprocessing

from smartwebsocketdata.GetterSpecificTokenCandleDataFromWebSocket import getterSpecificTokenCandleDataFromWebSocket


def eventLoopForAllITRCandlestickProperties(lock=multiprocessing.Lock(), isLive=False):
    startTime = time.time()
    lock.acquire()
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    lock.release()
    while datetime.datetime.now() - cv < exitTime:
        # get the id and symbol df
        with lock:
            gDf = getterRequiredSymbolAndTokenList()

        # getter past candle data
        if not isLive:
            with lock:
                pDs = getterPDS()
            lPDs = pDs.values.tolist()
        else:
            lPDs = [0, 0, 0, 0, 0, 0]

        # iterate gDf
        for index, row in gDf.iterrows():
            uid = row['id']
            symbol = row['symbol']
            token = row['token']
            with lock:
                psTime = getterSpecificCandleData(uid, symbol).loc[9, 'time']
            if isLive:
                sdf = getterSpecificTokenCandleDataFromWebSocket(token, lock)
                data = sdf.values.tolist()[0][:6]
            else:
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
