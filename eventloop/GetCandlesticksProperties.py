import pandas as pd
import time
from eventloop.QueueOperation import *
from candlestickdata.ATRCalculation import calculationForATR
from indicators.GetROCInPTM import getROCInPTM


def getCandlesticksProperties(sid, symbol, data):
    startTime = time.time()
    # get df (getter function)
    gdf = queueOperation(sid, symbol, data)

    # atr calculation
    atr, atrPer = calculationForATR(gdf)
    gdf.loc[9, 'atr'] = atrPer

    # Roc calculation part per 10 minute,
    # 100 ptm is equivalent to 1% change in one minute. And it will be negative when price decreases.
    roc = getROCInPTM(gdf)
    gdf.loc[9, 'roc'] = roc

    # setter function
    gdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)

    print(gdf)
    print(atr)
    print(atrPer)
    print(f"The execution time is {time.time() - startTime}")


for i in range(10):
    getCandlesticksProperties(1, "RELIANCE-EQ",
                              {0: "2023-10-20T09:25:00+05:30", 1: 23010.65, 2: 2312.25, 3: 2309.75, 4: 2311.95,
                               5: 25800})
