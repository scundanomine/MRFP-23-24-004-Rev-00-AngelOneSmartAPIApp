import pandas as pd
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList


def cleaningAndSettingPastTenCandleData():
    gDf = getterRequiredSymbolAndTokenList()
    for index, row in gDf.iterrows():
        uid = row['id']
        df = pd.DataFrame(columns=list(range(6)), index=list(range(10)))
        df[:] = 0
        df.to_csv(
            f"F:\\AT\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{uid}.csv",
            index=False)


# cleaningAndSettingPastTenCandleData()
