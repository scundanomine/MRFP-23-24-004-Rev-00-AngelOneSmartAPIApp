import pandas as pd
import time

from ohlcdata.GetterPastTenCandleDF import getterPastTenCandleDf


def createGSTDataFile(sid, symbol):
    # get df
    sdf = getterPastTenCandleDf(sid, symbol)

    # rename ohlc
    sdf.rename(columns={'0': "time", '1': "O", '2': "H", '3': "L", '4': "C", '5': "V"}, inplace=True)

    # add required columns
    new_cols = ['atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc', 'um', 'dm', 'rsi', 'sma']
    cols_to_add = [col for col in new_cols if col not in sdf.columns]
    sdf.loc[:, cols_to_add] = 0
    sdf["atr"] = 0
    sdf["bulRP"] = "none"
    sdf["berRP"] = "none"
    sdf["roc"] = 0
    sdf["rsi"] = 50
    sdf["um"] = 0
    sdf["dm"] = 0
    sdf["sma"] = 0

    # create import function
    sdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)
