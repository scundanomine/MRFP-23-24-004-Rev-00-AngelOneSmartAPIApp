import datetime
import multiprocessing
import time

import pandas as pd

from belliprogressionem.bellientry.GetEntryFlagUsingTrendingStrategy import getEntryFlagUsingTrendingStrategy
from belliprogressionem.belliexit.GetExitFlagUsingTrendingStrategy import getExitFlagUsingTrendingStrategy
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from position.GetterPositionList import getterPositionList


def getAllItrStrategyEntryAndExitFlags(lock=multiprocessing.Lock(), isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # getter entry flags from the belli progressionem
        # ebf, esf = getEntryFlagUsingTrendingStrategy(cv, isLive)
        getEntryFlagUsingTrendingStrategy(cv, isLive)

        # getter position list
        pLDf = getterPositionList()

        # getter exit flags
        getExitFlagUsingTrendingStrategy(cv, len(pLDf), isLive)

        time.sleep(0.01)

# getEntryList()
