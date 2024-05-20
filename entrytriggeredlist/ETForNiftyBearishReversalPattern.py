import time

from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.CheckBullishReversalCandle import checkBullishReversalCandle
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterCustomBlackListET import getterCustomBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForNiftyBearishReversalPatternForSell(lock, eTSF="T"):
    # get current resistance AI list
    rdf = getterAIList("NiftyAIList")

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
                # atr = row['atr']
                rsi = row['rsi0']

                # condition for 'sell'
                if eTSF == 'F':
                    # update the order type and upend the order list
                    row["ot"] = "sell"
                    row['oc'] = "ETFNiftyToSell"
                    row['srT'] = time.time()
                    with lock:
                        getterAppendAndSetterEntryTriggeredList(row)
                        # update the black list
                        getterUpdateAndSetterBlackListET(uid, 1)
    except Exception as e:
        print(f"Exception while entryTriggeredForNiftyBearishReversalPatternForSell: is {e}")
        time.sleep(1)
        entryTriggeredForNiftyBearishReversalPatternForSell(lock)

# entryTriggeredForBearishReversalPatternForSell()
