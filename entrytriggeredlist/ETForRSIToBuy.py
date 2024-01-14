from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForRSIToBuy(lock):
    # get current resistance AI list
    rdf = getterAIList("BuyerRSIAIList", lock)

    # getter ET black list
    bLDf = getterBlackListET(lock)

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
            if row['rsi0'] >= 30 and row['rsi0'] >= row['rsi1'] >= row["rsi2"] and (cTwo - cOne) >= 0.2*atr and row['roc0'] >= 1:
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "EntryTriggeredDueToRSIDivergenceForBuy"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)


# entryTriggeredForRSIToBuy()
