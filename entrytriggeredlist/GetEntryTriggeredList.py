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


def getEntryTriggeredList(lock=multiprocessing.Lock()):
    startTime = time.time()
    ctrA = 0
    lock.acquire()
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    lock.release()
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
        print(f"{ctrA} execution time for getting entry triggered list is {time.time() - startTime}")
        time.sleep(5)


# getEntryTriggeredList()
