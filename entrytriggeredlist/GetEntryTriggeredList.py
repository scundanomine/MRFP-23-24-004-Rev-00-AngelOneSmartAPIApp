from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from entrytriggeredlist.ETForBearishReversalPattern import entryTriggeredForBearishReversalPatternForSell
from entrytriggeredlist.ETForBullishReversalPattern import entryTriggeredForBullishReversalPatternForBuy
from entrytriggeredlist.ETForNiftyBearishReversalPattern import entryTriggeredForNiftyBearishReversalPatternForSell
from entrytriggeredlist.ETForNiftyBullishReversalPattern import entryTriggeredForNiftyBullishReversalPatternForBuy
from entrytriggeredlist.ETForNiftyRSIToBuy import entryTriggeredForNiftyRSIToBuy
from entrytriggeredlist.ETForNiftyRSIToSell import entryTriggeredForNiftyRSIToSell
from entrytriggeredlist.ETForRSIToBuy import entryTriggeredForRSIToBuy
from entrytriggeredlist.ETForRSIToSell import entryTriggeredForRSIToSell
from entrytriggeredlist.GetBlackListForET import getBlackListForET
import time
import datetime
import multiprocessing
import pandas as pd

from entrytriggeredlist.GetterPreCustomBlackListForET import getterPreCustomBlackListForET


def getEntryTriggeredList(lock=multiprocessing.Lock(), isLive=False):
    # startTime = time.time()
    # ctrA = 0
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()

    while datetime.datetime.now() - cv < exitTime:
        # get custom pre black list for ET
        getterPreCustomBlackListForET()

        # EL due to reversal pattern
        entryTriggeredForBullishReversalPatternForBuy(lock)
        entryTriggeredForBearishReversalPatternForSell(lock)

        # EL due to RSI
        entryTriggeredForRSIToBuy(lock)
        entryTriggeredForRSIToSell(lock)

        # EL due to reversal pattern
        entryTriggeredForNiftyBullishReversalPatternForBuy(lock)
        entryTriggeredForNiftyBearishReversalPatternForSell(lock)

        # EL due to RSI
        entryTriggeredForNiftyRSIToBuy(lock)
        entryTriggeredForNiftyRSIToSell(lock)

        # ctrA = ctrA + 1
        # if ctrA == 10:
        #     print(f"Execution time for getting entry triggered list (ET) is {time.time() - startTime}")
        #     ctrA = 0
        time.sleep(0.125)


# getEntryTriggeredList()
