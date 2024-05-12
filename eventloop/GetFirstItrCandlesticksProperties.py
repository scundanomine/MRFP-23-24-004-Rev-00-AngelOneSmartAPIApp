import pandas as pd
from candlestickdata.ATRCalculationWithoutThreading import calculationOfATRWithoutThreading
from candlestickdata.GetBearishReversalCandlestickPatternWithoutThreading import \
    getBearishReversalCandlestickPatternWithoutThreading
from candlestickdata.GetBullishReversalCandlestickPatternWithoutThreading import \
    getBullishReversalCandlestickPatternWithoutThreading
from candlestickdata.GetGSTDataWithoutThreading import getGSTDataWithoutThreading
from candlestickvolume.GetATRForVolume import getATRForVolume
from candlestickvolume.GetVolumeCandleSizeWithoutThreading import getVolumeCandleSizeWithoutThreading
from indicators.GetFirstItrROCInPTM import getFirstItrROCInPTM
from indicators.GetFirstItrSMAForNiftyIndex import getFirstItrSMAForNiftyIndex
from indicators.GetROCInPTM import getROCInPTM
from indicators.GetRSIValueWithoutThreading import getRSIValueWithoutThreading


def getFirstItrCandlesticksProperties(sid, symbol):
    # startTime = time.time()
    # get df (getter function)
    # gdf = queueOperation(sid, symbol, data)
    gdf = pd.read_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv")

    # atr calculation
    atr, atrPer = calculationOfATRWithoutThreading(gdf)
    # gdf.loc[9, 'atr'] = atr
    gdf['atr'] = atr
    gdf['atrPer'] = atrPer

    # Roc calculation part per 10 minute,
    # 100 ptm is equivalent to 1% change in 10 minute. And it will be negative when price decreases.
    gdf = getFirstItrROCInPTM(gdf)

    # rsi calculation
    gdf = getRSIValueWithoutThreading(gdf)
    # gdf.loc[9, 'rsi'] = rsi

    # calculation for volume Atr
    atrV = getATRForVolume(gdf)
    gdf['atrV'] = atrV

    # calculation for SMA for indexes
    # if token == 99926012:
    #     gdf = getFirstItrSMAForNiftyIndex(gdf)

    # calculation for volume size
    gdf = getVolumeCandleSizeWithoutThreading(gdf)

    # gst calculation
    gdf = getGSTDataWithoutThreading(gdf)

    # get bullish reversal pattern
    gdf = getBullishReversalCandlestickPatternWithoutThreading(gdf)

    # get bearish reversal pattern
    gdf = getBearishReversalCandlestickPatternWithoutThreading(gdf)

    # setter function
    gdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)

