import datetime
import time
import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from historicdata.GetHistoricDataWithQuery import getHistoricDataWithQuery
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from ohlcdata.GetterFDS import getterFDS
from pastthirtycandles.GetterSpecificPastThirtyCandlesData import getterSpecificPastThirtyCandlesData
from smartwebsocketdata.GetterSpecificTokenLivePartlyCandleDataFromWebSocket import \
    getterSpecificTokenLivePartlyCandleDataFromWebSocket


def getPastThirtyCandles(isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    date = datetime.datetime.today() - cv
    date = date.strftime("%Y-%m-%d")
    while datetime.datetime.now() - cv < exitTime:
        # getter symbol and token list
        sTDf = getterRequiredSymbolAndTokenList()
        currentTime = datetime.datetime.now() - cv
        toTime = currentTime + datetime.timedelta(minutes=1)
        reqTime = currentTime.strftime("%Y-%m-%dT%H:%M:00+05:30")
        for index, row in sTDf.iterrows():
            uid = row['id']
            symbol = row['symbol']
            token = row['token']
            if uid == 120:
                cdf = getterMarketStructureDf()
            else:
                cdf = getterSpecificCandleData(uid, symbol)
            tdf = getterSpecificPastThirtyCandlesData(uid, symbol)
            if cdf.loc[9, 'time'] == tdf.loc[28, 'time']:
                continue
            else:
                # queue operation for past thirty candles
                tdf = tdf.drop([0], axis=0)
                tdf.index = list(range(29))
                tdf.loc[28] = cdf.loc[9]
                tdf.loc[len(tdf)] = 0
                if isLive:
                    data = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token).iloc[0]
                else:
                    lstData = getHistoricDataWithQuery(currentTime, toTime, uid, date)
                    if not lstData:
                        data = {"0": reqTime, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
                    else:
                        try:
                            data = lstData[0]
                        except Exception as e:
                            print(f"exception while getting historic data for {uid} for process-2 is {e}")
                            data = {"0": reqTime, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
                lid = 29
                tdf.iloc[lid] = tdf.iloc[lid-1]
                tdf.loc[lid, "time"] = data['0']
                tdf.loc[lid, "O"] = data['1']
                tdf.loc[lid, "H"] = data['2']
                tdf.loc[lid, "L"] = data['3']
                tdf.loc[lid, "C"] = data['4']
                tdf.loc[lid, "V"] = data['5']
                tdf.to_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\pastthirtycandlewisedata\\{uid}_{symbol}.csv",
                    index=False)
        # ctrA = ctrA + 1
        # if ctrA == 10:
        #     print(f"Execution time for getting Entry List (EL) is {time.time() - startTime}")
        #     ctrA = 0
        time.sleep(1)


# getPastThirtyCandles()
