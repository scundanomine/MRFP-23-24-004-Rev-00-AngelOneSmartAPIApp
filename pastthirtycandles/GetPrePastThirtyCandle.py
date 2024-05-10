import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from pastthirtycandles.GetterSpecificDfForPastThirtyCandle import getterSpecificDfForPastThirtyCandle


def getPrePastThirtyCandle():
    # startTime = time.time()
    sTDf = getterRequiredSymbolAndTokenList()
    dfOne = getterSpecificDfForPastThirtyCandle("dfOne")
    dfTwo = getterSpecificDfForPastThirtyCandle("dfTwo")
    sdfOne = getterSpecificDfForPastThirtyCandle("sdfOne")
    sdfTwo = getterSpecificDfForPastThirtyCandle("sdfTwo")
    for index, row in sTDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        if row['id'] != 120:
            cdf = getterSpecificCandleData(uid, symbol)
            df = pd.concat([dfOne, cdf, dfTwo], ignore_index=True)
        else:
            cdf = getterMarketStructureDf()
            df = pd.concat([sdfOne, cdf, sdfTwo], ignore_index=True)

        df.to_csv(
            f"F:\\AT\\pastthirtycandles\\pastthirycandlesstate\\pastthirtycandlewisedata\\{uid}_{symbol}.csv", index=False)
    # print(f"Time taken: {time.time() - startTime}")


# getPrePastThirtyCandle()
