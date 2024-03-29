import pandas as pd
import time
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from pastthirtycandles.GetterDfOneForPastThirtyCandle import getterDfOneForPastThirtyCandle
from pastthirtycandles.GetterDfTwoForPastThirtyCandle import getterDfTwoForPastThirtyCandle


def getPrePastThirtyCandle():
    # startTime = time.time()
    sTDf = getterRequiredSymbolAndTokenList()
    dfOne = getterDfOneForPastThirtyCandle()
    dfTwo = getterDfTwoForPastThirtyCandle()
    for index, row in sTDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        cdf = getterSpecificCandleData(uid, symbol)
        df = pd.concat([dfOne, cdf, dfTwo], ignore_index=True)
        if row['id'] == 120:
            new_cols = ['emaOne', 'emaTwo', 'QOne', 'QTwo', 'QQOne', 'QQTwo', 'mTyp']
            cols_to_add = [col for col in new_cols if col not in df.columns]
            df.loc[:, cols_to_add] = 0
        df.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\pastthirtycandlewisedata\\{uid}_{symbol}.csv", index=False)
    # print(f"Time taken: {time.time() - startTime}")


# getPrePastThirtyCandle()
