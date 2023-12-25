from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForBullishReversalPatternForBuy(lock):
    # get current resistance AI list
    rdf = getterAIList("BullishReversalAIList", lock)
    # print(rdf)

    # getter ET black list
    bLDf = getterBlackListET(lock)
    # print(bLDf)

    for index, row in rdf.iterrows():
        uid = row['id']
        # condition of black listed
        if bLDf['bFlag'][uid - 1] == 1:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            atr = row['atr']

            # condition for sell
            if (cTwo - cOne) >= 0.25 * atr and checkBullishReversalPattern(row["bulRP"]):
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "EntryTriggeredDueToBullishReversalPatternToBuy"
                lock.acquire()
                getterAppendAndSetterEntryTriggeredList(row)
                # update the black list
                getterUpdateAndSetterBlackListET(uid, 1)
                lock.release()

# entryTriggeredForBullishReversalPatternForBuy()
