import time

from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBullishReversalCandle import checkBullishReversalCandle
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterCustomBlackListET import getterCustomBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForRSIToSell(lock):
    # get current resistance AI list
    rdf = getterAIList("SellerRSIAIList")

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
                # condition for sell
                if uid <= 50 and row['rsi0'] < row['rsi1'] < row['rsi2'] and (cTwo - cOne) <= -0.2*atr and row['roc0'] >= 15 and not checkBullishReversalCandle(row["t"]):
                    # update the order type and upend the order list
                    row["ot"] = "sell"
                    row['oc'] = "ETFRSIDivergenceForSell"
                    row['srT'] = time.time()
                    with lock:
                        getterAppendAndSetterEntryTriggeredList(row)
                        # update the black list
                        getterUpdateAndSetterBlackListET(uid, 1)
    except Exception as e:
        print(f"Exception while entryTriggeredForRSIToSell: is {e}")
        time.sleep(1)
        entryTriggeredForRSIToSell(lock)


# entryTriggeredForRSIToSell()
