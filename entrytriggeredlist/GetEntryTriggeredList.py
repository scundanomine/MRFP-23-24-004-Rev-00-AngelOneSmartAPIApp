from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entrytriggeredlist.ETForBearishReversalPattern import entryTriggeredForBearishReversalPatternForSell
from entrytriggeredlist.ETForBullishReversalPattern import entryTriggeredForBullishReversalPatternForBuy
from entrytriggeredlist.ETForRSIToBuy import entryTriggeredForRSIToBuy
from entrytriggeredlist.ETForRSIToSell import entryTriggeredForRSIToSell
from entrytriggeredlist.ETForResistancePivot import entryTriggeredForResistancePivot
from entrytriggeredlist.ETForSupportPivot import entryTriggeredForSupportPivot
from entrytriggeredlist.ETForTopGainerToBuy import entryTriggeredForTopGainerToBuy
from entrytriggeredlist.ETForTopLoserToSell import entryTriggeredForTopLoserToSell
from entrytriggeredlist.GetBlackListForET import getBlackListForET
import time
import datetime
import multiprocessing
import pandas as pd


def getEntryTriggeredList(lock=multiprocessing.Lock(), isLive=False):
    startTime = time.time()
    ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # get black list for ET
        getBlackListForET(lock)

        # EL due support and resistance
        entryTriggeredForResistancePivot(lock)
        entryTriggeredForSupportPivot(lock)

        # EL due to top gainer and loser
        entryTriggeredForTopGainerToBuy(lock)
        entryTriggeredForTopLoserToSell(lock)

        # EL due RSI
        entryTriggeredForRSIToBuy(lock)
        entryTriggeredForRSIToSell(lock)

        # EL due to reversal pattern
        entryTriggeredForBearishReversalPatternForSell(lock)
        entryTriggeredForBullishReversalPatternForBuy(lock)
        ctrA = ctrA + 1
        if ctrA == 10:
            print(f"Execution time for getting entry triggered list (ET) is {time.time() - startTime}")
            ctrA = 0
        time.sleep(1)


# getEntryTriggeredList()
