from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET
import multiprocessing


def entryTriggeredForBullishReversalPatternForBuy(lock=multiprocessing.Lock()):
    # get current resistance AI list
    rdf = getterAIList("BullishReversalAIList")

    # getter ET black list
    bLDf = getterBlackListET()

    for index, row in rdf.iterrows():
        uid = row['id']
        # condition of black listed
        if bLDf['bFlag'][uid - 1] == 1:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            # atr = row['atr']
            rsi = row['rsi0']

            # condition for sell
            if cTwo > cOne and checkBullishReversalPattern(row["bulRP"]) and rsi <= 30:
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "EntryTriggeredDueToBullishReversalPatternToBuy"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)


# entryTriggeredForBullishReversalPatternForBuy()
