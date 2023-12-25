from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForRSIToBuy(lock):
    # get current resistance AI list
    rdf = getterAIList("BuyerRSIAIList", lock)
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
            # condition for buy
            if row['rsi0'] >= 70 and row['rsi0'] >= row['rsi1'] and (cTwo - cOne) >= 0.2*atr and row['roc0'] >= 15:
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "EntryTriggeredDueToRSIDivergenceForBuy"
                lock.acquire()
                getterAppendAndSetterEntryTriggeredList(row)
                # update the black list
                getterUpdateAndSetterBlackListET(uid, 1)
                lock.release()


# entryTriggeredForRSIToBuy()
