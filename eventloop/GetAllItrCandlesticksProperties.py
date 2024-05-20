from candlestickdataallitr.AllItrATRCalculation import calculationAllItrForATR
from candlestickdataallitr.GetAllItrBearishReversalCandlestickPatternWithoutThreading import \
    getAllItrBearishReversalCandlestickPatternWithoutThreading
from candlestickdataallitr.GetAllItrBullishReversalCandlestickPatternWithoutThreading import \
    getAllItrBullishReversalCandlestickPatternWithoutThreading
from candlestickdataallitr.GetAllItrGSTData import getAllItrCandlestickGSTData
from candlestickvolume.GetAllItrATRForVolume import getAllItrATRForVolume
from candlestickvolume.GetAllItrVolumeCandleSize import getAllItrVolumeCandleSize
from eventloop.QueueOperation import *
from indicators.GetAllItrRSIValue import getAllItrRSIValue
from indicators.GetAllItrSMAForNiftyIndex import getAllItrSMAForNiftyIndex
from indicators.GetROCInPTM import getROCInPTM


def getAllItrCandlesticksProperties(sid, symbol, data):
    # startTime = time.time()

    # get df (getter function)
    gdf = queueOperation(sid, symbol, data)

    # atr calculation
    atr, atrPer = calculationAllItrForATR(gdf)
    gdf.loc[9, 'atr'] = atr
    gdf.loc[9, 'atrPer'] = atrPer

    # Roc calculation part per 10 minute,
    # 100 ptm is equivalent to 1% change in one minute. And it will be negative when price decreases.
    roc = getROCInPTM(gdf)
    gdf.loc[9, 'roc'] = roc

    # rsi calculation
    rsi = getAllItrRSIValue(gdf)
    gdf.loc[9, 'rsi'] = rsi

    # calculation for volume Atr
    atrV = getAllItrATRForVolume(gdf)
    gdf.loc[9, 'atrV'] = atrV

    # calculation for SMA for indexes
    # if token == 99926000:
    #     sma = getAllItrSMAForNiftyIndex(gdf)
    #     gdf.loc[9, 'sma'] = sma

    # calculation for volume size
    gdf = getAllItrVolumeCandleSize(gdf)

    # gst calculation
    gdf = getAllItrCandlestickGSTData(gdf)

    # get bullish reversal pattern
    gdf = getAllItrBullishReversalCandlestickPatternWithoutThreading(gdf)

    # get bearish reversal pattern
    gdf = getAllItrBearishReversalCandlestickPatternWithoutThreading(gdf)

    # setter function
    gdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)

