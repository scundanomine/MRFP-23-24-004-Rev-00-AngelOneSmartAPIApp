import datetime
import time
import pandas as pd
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterReportDateForRR import getterReportDateForRR
from commonudm.GetterTimeDelta import getterTimeDelta
from position.GetterPositionId import getterPositionId
from position.GetterPositionIdForSpecificDate import getterPositionIdForSpecificDate
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
    reportDate = getterReportDateForRR()
    while datetime.datetime.now() - cv < exitTime:
        # getter position id
        pid = getterPositionIdForSpecificDate(reportDate)

        # Population of black list
        generatorChartBlackListRR(pid)

        # population of position plots and market plot
        generatorPositionCandlePlotFileRR()

        # population of exit plots and market plot
        generatorExitCandlePlotFileRR()

        # print(f"Execution time for Getting Records (RR) is {time.time() - startTime}")
        time.sleep(20)


# getAIListWithoutUdf()
