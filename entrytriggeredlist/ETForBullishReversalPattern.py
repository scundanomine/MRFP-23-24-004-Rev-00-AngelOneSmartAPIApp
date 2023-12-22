import time
from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList


def entryTriggeredForBullishReversalPatternForBuy(lock):
    # startTime = time.time()

    # get current resistance AI list
    rdf = getterAIList("BullishReversalAIList", lock)
    # print(rdf)

    # getter ET black list
    bLDf = getterBlackListET(lock)
    # print(bLDf)

    # getter Entry Triggered list
    oLDf = getterEntryTriggeredList(lock)
    # print(oLDf)

    for index, row in rdf.iterrows():
        uid = row['id']
        # condition of black listed
        if bLDf['bFlag'][uid-1]:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            atr = row['atr']

            # condition for sell
            if (cTwo - cOne) >= 0.25*atr and checkBullishReversalPattern(row["bulRP"]):
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "EntryTriggeredDueToBullishReversalPatternToBuy"
                oLDf.loc[len(oLDf)] = row
                # update the black list
                bLDf.loc[uid + 1, 'bFlag'] = True

            # condition for no buy or sale
            else:
                pass

    # setter for ET black list
    lock.acquire()
    bLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)

    # setter for Entry Triggered list
    oLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv", index=False)
    lock.release()
    # print(f"execution time is {time.time() - startTime}")


# entryTriggeredForBullishReversalPatternForBuy()
