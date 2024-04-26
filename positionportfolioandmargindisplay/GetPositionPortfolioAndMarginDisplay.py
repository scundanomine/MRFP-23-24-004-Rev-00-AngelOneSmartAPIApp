import datetime
import time
import pandas as pd
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from positionportfolioandmargindisplay.ClockForReferenceTime import clockForReferenceTime
from positionportfolioandmargindisplay.DisplayPastFiveMarketTrend import displayPastFiveMarketTrend
from positionportfolioandmargindisplay.GetMarginDisplay import getMarginDisplay
from positionportfolioandmargindisplay.GetPortfolioDisplay import getPortfolioDisplay
from positionportfolioandmargindisplay.GetPositionDisplay import getPositionDisplay


def getPositionPortfolioAndMarginDisplay(isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # pastime clock
        clockForReferenceTime(cv)

        # getter margin display
        getMarginDisplay()

        # getter portfolio display
        getPortfolioDisplay()

        # display for past last trend type
        displayPastFiveMarketTrend(cv)

        # getter position display
        getPositionDisplay()

        # ctrA = ctrA + 1
        # if ctrA == 2:
        #     print(
        #         f"Execution time for getting Position, Portfolio And Margin Display (PPM) is {time.time() - startTime}")
        #     ctrA = 0
        time.sleep(2)


# getPositionPortfolioAndMarginDisplay()
