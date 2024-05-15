import multiprocessing
import time
from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBearishReversalCandle import checkBearishReversalCandle
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterCustomBlackListET import getterCustomBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForBullishReversalPatternForBuy(lock=multiprocessing.Lock()):
    # get current resistance AI list
    rdf = getterAIList("BullishReversalAIList")

    # getter ET black list
    bLDf = getterBlackListET()
    cBLDf = getterCustomBlackListET()
    try:
        for index, row in rdf.iterrows():
            uid = row['id']
            # condition of black listed
            if bLDf.loc[uid-1, 'bFlag'] == 1 or cBLDf.loc[uid-1, 'bFlag'] == 1:
                continue
            else:
                cOne = row['CC1']
                cTwo = row['CC2']
                # atr = row['atr']
                # rsi = row['rsi0']

                # condition for buy
                if cTwo > cOne and checkBullishReversalPattern(row["bulRP"]) and row['g'] == 'green' and row['roc0'] <= -15 and not checkBearishReversalCandle(row["t"]):
                    # update the order type and upend the order list
                    row["ot"] = "buy"
                    row['oc'] = "ETFBullishReversalPatternToBuy"
                    row['srT'] = time.time()
                    with lock:
                        getterAppendAndSetterEntryTriggeredList(row)
                        # update the black list
                        getterUpdateAndSetterBlackListET(uid, 1)
    except Exception as e:
        print(f"Exception while entryTriggeredForBullishReversalPatternForBuy: is {e}")
        time.sleep(1)
        entryTriggeredForBullishReversalPatternForBuy(lock)


# entryTriggeredForBullishReversalPatternForBuy()
