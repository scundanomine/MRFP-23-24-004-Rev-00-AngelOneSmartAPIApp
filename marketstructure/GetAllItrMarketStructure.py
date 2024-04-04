import datetime
import time
import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from marketstructure.GetAllItrEMAAndDerivativesForNiftyIndex import getAllItrEMAAndDerivativesForNiftyIndex
from marketstructure.GetAllItrMarketStrength import getAllItrMarketStrength
from marketstructure.GetAllItrMarketTimeOfTrend import getAllItrMarketTimeOfTrend
from marketstructure.GetAllItrMarketTrend import getAllItrMarketTrend
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getAllItrMarketStructure(isLive=False):
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        df = getterMarketStructureDf()
        cdf = getterSpecificCandleData(120, "Nifty 100")
        if cdf.loc[9, 'time'] == df.loc[9, 'time']:
            time.sleep(1 / 100)
        else:
            # queue operation for past thirty candles
            df = df.drop(0, axis=0)
            df.index = list(range(9))
            df.loc[len(df)] = 0
            for name, values in cdf.items():
                df.loc[9, name] = cdf.loc[9, name]
            # calculation for EMAs and their derivatives
            df = getAllItrEMAAndDerivativesForNiftyIndex(df)
            df = getAllItrMarketTrend(df)
            df = getAllItrMarketStrength(df)
            df = getAllItrMarketTimeOfTrend(df)
            df = df.round(decimals=2)
            df.to_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
                index=False)


# getAllItrMarketStructure()
