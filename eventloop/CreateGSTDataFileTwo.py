import pandas as pd
import time

from commonudm.GetterDummyDf import getterDummyDf
from ohlcdata.GetterPastTenCandleDF import getterPastTenCandleDf


def createGSTDataFileTwo(sid, symbol):
    # get df
    df = getterPastTenCandleDf(sid)

    sdf = getterDummyDf()

    # create import function
    sdf.to_csv(
        f"F:\\AT\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)
