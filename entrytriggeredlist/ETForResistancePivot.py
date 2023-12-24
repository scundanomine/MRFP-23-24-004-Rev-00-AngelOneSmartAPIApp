import time
from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
import multiprocessing


def entryTriggeredForResistancePivot(lock=multiprocessing.Lock()):
    # startTime = time.time()

    # get current resistance AI list
    rdf = getterAIList("ResistanceAIList", lock)
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
        if bLDf['bFlag'][uid-1] == 1:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            rV = row['srV']
            atr = row['atr']
            # condition for buy
            if cTwo >= rV and cOne >= rV and (cTwo - cOne) >= 0.25*atr and row['rsi0'] >= 60:
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "EntryTriggeredDueToResistancePivot"
                oLDf.loc[len(oLDf)] = row
                # update the black list
                bLDf.loc[uid-1, 'bFlag'] = 1

            # condition for sell
            elif cTwo <= rV and cOne <= rV and (cTwo - cOne) <= -0.25*atr and checkBearishReversalPattern(row["berRP"]):
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "EntryTriggeredDueToResistancePivot"
                oLDf.loc[len(oLDf)] = row
                # update the black list
                bLDf.loc[uid-1, 'bFlag'] = 1

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


# entryTriggeredForResistancePivot()
