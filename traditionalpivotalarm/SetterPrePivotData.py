import pandas as pd

from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterStockQtn import getterStockQtn
from ohlcdata.GetterPastTenCandleDF import getterPastTenCandleDf


def setterPrePivotData():
    n = getterStockQtn()
    gDf = getterRequiredSymbolAndTokenList()
    pivDf = pd.DataFrame(columns=['id', 'prevT', 'C', 'alarmTimer', 'refT', 'srT', 'srV', 'nSR', 'GL'], index=list(range(n)))
    pivDf[:] = 0
    pivDf["srT"] = "none"
    pivDf['id'] = list(range(1, n + 1))
    for index, row in gDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        close = getterPastTenCandleDf(uid).loc[9, '4']
        pivDf.loc[index, 'C'] = close

    pivDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\PivotData.csv",
        index=False)
    return pivDf


# print(setterPrePivotData())
