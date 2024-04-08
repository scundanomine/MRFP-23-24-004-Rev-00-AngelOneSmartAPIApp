import time

from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBearishReversalCandle import checkBearishReversalCandle
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterCustomBlackListET import getterCustomBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForRSIToBuy(flagBearish, lock):
    # get current resistance AI list
    rdf = getterAIList("BuyerRSIAIList")

    # getter ET black list
    bLDf = getterBlackListET()
    cBLDf = getterCustomBlackListET()
    try:
        for index, row in rdf.iterrows():
            uid = row['id']
            # condition of black listed
            if bLDf['bFlag'][uid - 1] == 1 or cBLDf['bFlag'][uid - 1] == 1:
                continue
            else:
                cOne = row['CC1']
                cTwo = row['CC2']
                atr = row['atr']
                # condition for buy
                if not flagBearish and row['rsi0'] >= row['rsi1'] >= row["rsi2"] and (cTwo - cOne) >= 0.2*atr and row['roc0'] <= -15 and not checkBearishReversalCandle(row["t"]):
                    # update the order type and upend the order list
                    row["ot"] = "buy"
                    row['oc'] = "ETFRSIDivergenceForBuy"
                    row['srT'] = time.time()
                    with lock:
                        getterAppendAndSetterEntryTriggeredList(row)
                        # update the black list
                        getterUpdateAndSetterBlackListET(uid, 1)
    except Exception as e:
        print(f"Exception while entryTriggeredForRSIToBuy: is {e}")
        time.sleep(1)
        entryTriggeredForRSIToBuy(flagBearish, lock)


# entryTriggeredForRSIToBuy()
