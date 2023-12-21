import pandas as pd
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList


def cleaningAndSettingPastTenCandleData():
    gDf = getterRequiredSymbolAndTokenList()
    for index, row in gDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        df = pd.DataFrame(columns=list(range(6)), index=list(range(10)))
        df[:] = 0
        df.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{uid}_{symbol}.csv",
            index=False)


# cleaningAndSettingPastTenCandleData()
