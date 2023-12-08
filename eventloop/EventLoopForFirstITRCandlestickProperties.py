from commonudm.GetSymbolAndToken import getSymbolAndToken
from eventloop.CreateGSTDataFile import createGSTDataFile
import time
from eventloop.GetFirstItrCandlesticksProperties import getFirstItrCandlesticksProperties


def eventLoopForFirstITRCandlestickProperties(n=300):
    startTime = time.time()
    # get the id and symbol df
    gDf = getSymbolAndToken()
    # delete all row except n and column except few
    dfSize = len(gDf)
    gDf = gDf.drop(labels=range(n, dfSize), axis=0)
    gDf = gDf.loc[:, ['id', 'symbol']]
    # print(gDf)

    # iterate gDf
    for index, row in gDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        # initial file list
        createGSTDataFile(uid, symbol)
        # calculation for candle properties
        getFirstItrCandlesticksProperties(uid, symbol)

    # print(f"the of execution is {time.time() - startTime}")


# eventLoopForFirstITRCandlestickProperties()
