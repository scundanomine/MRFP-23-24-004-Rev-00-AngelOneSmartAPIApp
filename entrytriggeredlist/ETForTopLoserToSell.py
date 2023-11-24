import time
from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList


def entryTriggeredForTopLoserToSell(niftySize=300):
    startTime = time.time()

    # get current resistance AI list
    rdf = getterAIList("TopLoserAIList")
    print(rdf)

    # getter ET black list
    bLDf = getterBlackListET()
    print(bLDf)

    # getter Entry Triggered list
    oLDf = getterEntryTriggeredList()
    print(oLDf)

    for index, row in rdf.iterrows():
        uid = row['id']
        # condition of black listed
        if bLDf['bFlag'][uid-1]:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            atr = row['atr']
            # condition for buy
            if row['rsi0'] <= 30 and row['rsi0'] <= row['rsi1'] and (cTwo - cOne) <= -0.2*atr and row['roc0'] <= -15:
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "EntryTriggeredDueToTopLoserForSell"
                oLDf.loc[len(oLDf)] = row
                # update the black list
                bLDf.loc[uid+1, 'bFlag'] = True

            # condition for no buy or sale
            else:
                pass

    # setter for ET black list
    bLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)

    # setter for Entry Triggered list
    oLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv", index=False)

    print(f"execution time is {time.time() - startTime}")


entryTriggeredForTopLoserToSell()
