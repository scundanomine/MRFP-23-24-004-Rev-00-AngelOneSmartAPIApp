import pandas as pd
import time

from commonudm.GetterDummyDf import getterDummyDf
from ohlcdata.GetterPastTenCandleDF import getterPastTenCandleDf


def createGSTDataFileTwo(sid, symbol):
    # get df
    df = getterPastTenCandleDf(sid, symbol)

    sdf = getterDummyDf()

    # create import function
    sdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)
