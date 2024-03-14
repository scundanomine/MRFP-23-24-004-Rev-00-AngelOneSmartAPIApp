import datetime
import time
import pandas as pd
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from position.GetterPositionId import getterPositionId
from readandrecord.GeneratorChartBlackListRR import generatorChartBlackListRR
from readandrecord.GeneratorExitCandlePlotFileRR import generatorExitCandlePlotFileRR
from readandrecord.GeneratorPositionCandlePlotFileRR import generatorPositionCandlePlotFileRR


def getRecords(isLive=False):
    # startTime = time.time()
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # getter position id
        pid = getterPositionId()

        # Population of black list
        generatorChartBlackListRR(pid)

        # population of position plots
        generatorPositionCandlePlotFileRR('positioncandles', 'positionplots')

        # population of market position plots
        generatorPositionCandlePlotFileRR('positionmcandles', 'positionmplots')

        # population of exit plots
        generatorExitCandlePlotFileRR('exitcandles', 'exitplots')

        # population of market exit plots
        generatorExitCandlePlotFileRR('exitmcandles', 'exitmplots')

        # print(f"Execution time for Getting Records (RR) is {time.time() - startTime}")
        time.sleep(20)


# getAIListWithoutUdf()
