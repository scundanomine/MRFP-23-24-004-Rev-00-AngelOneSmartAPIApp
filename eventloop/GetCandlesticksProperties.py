from candlestickdata.GetBearishReversalCandlestickPattern import getBearishReversalCandlestickPattern
from candlestickdata.GetBullishReversalCandlestickPattern import getBullishReversalCandlestickPattern
from eventloop.QueueOperation import *
from candlestickdata.ATRCalculation import calculationForATR
from indicators.GetROCInPTM import getROCInPTM
from indicators.GetRSIValue import getRSIValue
from candlestickdata.GetGSTData import getCandlestickGSTData
from candlestickvolume.GetATRForVolume import getATRForVolume
from candlestickvolume.GetVolumeCandleSize import getVolumeCandleSize


def getCandlesticksProperties(sid, symbol, data):
    startTime = time.time()
    # get df (getter function)
    gdf = queueOperation(sid, symbol, data)

    # atr calculation
    atr, atrPer = calculationForATR(gdf)
    # gdf.loc[9, 'atr'] = atr
    gdf['atr'] = atr

    # Roc calculation part per 10 minute,
    # 100 ptm is equivalent to 1% change in one minute. And it will be negative when price decreases.
    roc = getROCInPTM(gdf)
    gdf.loc[9, 'roc'] = roc

    # rsi calculation
    rsi = getRSIValue(gdf)
    gdf.loc[9, 'rsi'] = rsi

    # calculation for volume Atr
    atrV = getATRForVolume(gdf)
    gdf['atrV'] = atrV

    # calculation for volume size
    gdf = getVolumeCandleSize(gdf)

    # gst calculation
    gdf = getCandlestickGSTData(gdf)

    # get bullish reversal pattern
    gdf = getBullishReversalCandlestickPattern(gdf)

    # get bearish reversal pattern
    gdf = getBearishReversalCandlestickPattern(gdf)

    # setter function
    gdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)

    print(gdf)
    print(atr)
    print(atrPer)
    print(f"The execution time is {time.time() - startTime}")


for i in range(1):
    getCandlesticksProperties(1, "RELIANCE-EQ",
                              {0: "2023-10-20T09:25:00+05:30", 1: 23010.65, 2: 2312.25, 3: 2309.75, 4: 2311.95,
                               5: 25800})
