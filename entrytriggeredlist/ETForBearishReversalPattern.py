from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForBearishReversalPatternForSell(lock):
    # get current resistance AI list
    rdf = getterAIList("BearishReversalAIList", lock)
    # print(rdf)

    # getter ET black list
    bLDf = getterBlackListET(lock)
    # print(bLDf)

    for index, row in rdf.iterrows():
        uid = row['id']
        # condition of black listed
        if bLDf['bFlag'][uid-1] == 1:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            atr = row['atr']

            # condition for sell
            if (cTwo - cOne) <= -0.25*atr and checkBearishReversalPattern(row["berRP"]):
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "EntryTriggeredDueToBearishReversalPatternToSell"
                lock.acquire()
                getterAppendAndSetterEntryTriggeredList(row)
                # update the black list
                getterUpdateAndSetterBlackListET(uid, 1)
                lock.release()


# entryTriggeredForBearishReversalPatternForSell()
