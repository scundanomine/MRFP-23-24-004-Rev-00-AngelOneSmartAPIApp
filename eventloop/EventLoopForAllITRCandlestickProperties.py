import datetime
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
import time
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from eventloop.GetAllItrCandlesticksProperties import getAllItrCandlesticksProperties
from ohlcdata.GetterPDS import getterPDS
import multiprocessing
import pandas as pd

from smartwebsocketdata.GetterSpecificTokenCandleDataFromWebSocket import getterSpecificTokenCandleDataFromWebSocket


def eventLoopForAllITRCandlestickProperties(isLive=False):
    startTime = time.time()
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # get the id and symbol df
        gDf = getterRequiredSymbolAndTokenList()

        # getter past candle data
        if not isLive:
            pDs = getterPDS()
            lPDs = pDs.values.tolist()
        else:
            lPDs = [0, 0, 0, 0, 0, 0]

        # iterate gDf
        for index, row in gDf.iterrows():
            uid = row['id']
            symbol = row['symbol']
            token = row['token']
            psTime = getterSpecificCandleData(uid, symbol).loc[9, 'time']
            if isLive:
                sdf = getterSpecificTokenCandleDataFromWebSocket(token)
                data = sdf.values.tolist()[0][:6]
            else:
                data = lPDs[uid - 1]
            fsTime = data[0]
            if psTime == fsTime:
                continue
            else:
                # calculation for candle properties
                getAllItrCandlesticksProperties(uid, symbol, data, token)
        print(f"Execution time for All Itr candle properties (CP) is {time.time() - startTime}")
        time.sleep(5)


# eventLoopForAllITRCandlestickProperties()
