from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from eventloop.CreateGSTDataFile import createGSTDataFile
import time
from eventloop.GetFirstItrCandlesticksProperties import getFirstItrCandlesticksProperties


def eventLoopForFirstITRCandlestickProperties():
    # startTime = time.time()
    # get the id and symbol df
    gDf = getterRequiredSymbolAndTokenList()

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
