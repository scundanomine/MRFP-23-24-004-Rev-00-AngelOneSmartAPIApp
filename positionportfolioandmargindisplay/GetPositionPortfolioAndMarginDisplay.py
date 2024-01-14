import xlwings as xw
import pandas as pd
import multiprocessing
import time
import datetime
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from positionportfolioandmargindisplay.GetMarginDisplay import getMarginDisplay
from positionportfolioandmargindisplay.GetPortfolioDisplay import getPortfolioDisplay
from positionportfolioandmargindisplay.GetPositionDisplay import getPositionDisplay


def getPositionPortfolioAndMarginDisplay(lock=multiprocessing.Lock()):
    startTime = time.time()
    ctrA = 0
    with lock:
        cv = getterTimeDelta()
        exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # getter margin display
        getMarginDisplay(lock)

        # getter portfolio display
        getPortfolioDisplay(lock)

        # getter position display
        getPositionDisplay(lock)

        ctrA = ctrA + 1
        if ctrA == 2:
            print(
                f"Execution time for getting Position, Portfolio And Margin Display (PPM) is {time.time() - startTime}")
            ctrA = 0
        time.sleep(4)


# getPositionPortfolioAndMarginDisplay()
