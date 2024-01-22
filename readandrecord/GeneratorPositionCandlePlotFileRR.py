import mplfinance as mpf
import pandas as pd
from readandrecord.GetterDfFromSpecificRRState import getterDfFromSpecificRRState
from readandrecord.GetterPECBListRR import getterPECBListRR


def generatorPositionCandlePlotFileRR():
    # getter position chart black list
    pEDf = getterPECBListRR()
    for index, row in pEDf.iterrows():
        pid = row['pid']
        if row['flagPC'] == 1:
            continue
        else:
            # get position candle for specific pid
            pCDf = getterDfFromSpecificRRState('positioncandles', pid)
            # process position candle for specific pid

