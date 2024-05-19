import datetime
import time
import pandas as pd
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterReportDateForRR import getterReportDateForRR
from commonudm.GetterTimeDelta import getterTimeDelta
from positionportfolioandmargindisplay.ClockForReferenceTime import clockForReferenceTime
from positionportfolioandmargindisplay.GetMarginDisplay import getMarginDisplay
from positionportfolioandmargindisplay.GetPortfolioDisplay import getPortfolioDisplay
from positionportfolioandmargindisplay.GetPositionDisplay import getPositionDisplay
from positionportfolioandmargindisplay.GetPositionIdDisplay import getPositionIdDisplay


def getPositionPortfolioAndMarginDisplay(isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    reportDate = getterReportDateForRR()
    while datetime.datetime.now() - cv < exitTime:
        # pastime clock
        clockForReferenceTime(cv)

        # getter margin display
        getMarginDisplay()

        # getter portfolio display
        getPortfolioDisplay()

        # getter position id display
        getPositionIdDisplay(reportDate)

        # getter position display
        getPositionDisplay()

        time.sleep(2)


# getPositionPortfolioAndMarginDisplay()
