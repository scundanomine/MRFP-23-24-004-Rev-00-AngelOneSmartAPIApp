import datetime
import time
import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from pastthirtycandles.GetterSpecificPastThirtyCandlesData import getterSpecificPastThirtyCandlesData


def getPastThirtyCandles(isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # getter symbol and token list
        sTDf = getterRequiredSymbolAndTokenList()
        for index, row in sTDf.iterrows():
            uid = row['id']
            symbol = row['symbol']
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
                for name, values in cdf.items():
                    tdf.loc[29, name] = cdf.loc[9, name]
                tdf.to_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\pastthirtycandlewisedata\\{uid}_{symbol}.csv",
                    index=False)
        # ctrA = ctrA + 1
        # if ctrA == 10:
        #     print(f"Execution time for getting Entry List (EL) is {time.time() - startTime}")
        #     ctrA = 0
        time.sleep(1)


# getPastThirtyCandles()
