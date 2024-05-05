import datetime
import time
import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from eventloop.GetAllItrCandlesticksProperties import getAllItrCandlesticksProperties
from historicdata.GetHistoricDataWithQuery import getHistoricDataWithQuery
from smartwebsocketdata.GetterSpecificTokenCandleDataFromWebSocket import getterSpecificTokenCandleDataFromWebSocket


def eventLoopForAllITRCandlestickProperties(isLive=False):
    # startTime = time.time()
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    date = datetime.datetime.today() - cv
    date = date.strftime("%Y-%m-%d")
    while datetime.datetime.now() - cv < exitTime:
        # get the id and symbol df
        gDf = getterRequiredSymbolAndTokenList()
        currentTime = datetime.datetime.now() - cv
        reqTime = currentTime.strftime("%Y-%m-%dT%H:%M:00+05:30")
        # iterate gDf
        for index, row in gDf.iterrows():
            uid = row['id']
            symbol = row['symbol']
            token = row['token']
            psTime = getterSpecificCandleData(uid, symbol).loc[9, 'time']
            if psTime == reqTime:
                continue
            else:
                if isLive:
                    sdf = getterSpecificTokenCandleDataFromWebSocket(token)
                    data = sdf.values.tolist()[0][:6]
                else:
                    toTime = currentTime + datetime.timedelta(minutes=1)
                    lstData = getHistoricDataWithQuery(currentTime, toTime, uid, date)
                    if not lstData:
                        data = {"0": reqTime, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
                    else:
                        try:
                            data = lstData[0]
                        except Exception as e:
                            print(f"exception while getting historic data for {uid} for process-2 is {e}")
                            data = {"0": reqTime, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}

                # calculation for candle properties
                getAllItrCandlesticksProperties(uid, symbol, data)
        # print(f"Execution time for All Itr candle properties (CP) is {time.time() - startTime}")
        time.sleep(0.05)


# eventLoopForAllITRCandlestickProperties()
