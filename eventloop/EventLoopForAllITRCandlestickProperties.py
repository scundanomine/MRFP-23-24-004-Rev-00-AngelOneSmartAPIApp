from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetSymbolAndToken import getSymbolAndToken
import time
from eventloop.GetAllItrCandlesticksProperties import getAllItrCandlesticksProperties
from ohlcdata.GetterPDS import getterPDS


def eventLoopForAllITRCandlestickProperties(n=300):
    startTime = time.time()
    # get the id and symbol df
    gDf = getSymbolAndToken()
    # delete all row except n and column except few
    dfSize = len(gDf)
    gDf = gDf.drop(labels=range(n, dfSize), axis=0)
    gDf = gDf.loc[:, ['id', 'symbol']]
    # print(gDf)
    # getter past candle data
    pDs = getterPDS()
    lPDs = pDs.values.tolist()

    # iterate gDf
    for index, row in gDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        psTime = getterSpecificCandleData(uid, symbol).loc[9, 'time']
        data = lPDs[uid-1]
        fsTime = data[0]
        if psTime == fsTime:
            continue
        else:
            # calculation for candle properties
            getAllItrCandlesticksProperties(uid, symbol, data)

    # print(f"the of execution is {time.time() - startTime}")


# eventLoopForAllITRCandlestickProperties()
