import time
from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.BlackListET import getterBlackListET
from orderlist.GetterOrderList import getterOrderList


def entryTriggeredForRSIToSell(niftySize=300):
    startTime = time.time()

    # get current resistance AI list
    rdf = getterAIList("SellerRSIAIList")
    print(rdf)

    # getter ET black list
    bLDf = getterBlackListET()
    print(bLDf)

    # getter order list
    oLDf = getterOrderList()
    print(oLDf)

    for row in rdf:
        uid = row['id']
        # condition of black listed
        if uid in bLDf['id']:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            atr = row['atr']
            # condition for buy
            if row['rsi0'] <= 30 and row['rsi0'] <= row['rsi1'] and (cTwo - cOne) <= -0.2*atr and row['roc0'] <= -15:
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "EntryTriggeredDueToRSIDivergenceForSell"
                oLDf.loc[len(oLDf)] = row
                # update the black list
                bLDf.loc[uid+1, 'bFlag'] = True

            # condition for no buy or sale
            else:
                pass

    # setter for ET black list
    bLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)

    # setter for Order list black list
    oLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\orderlist\\olstate\\OrderList.csv", index=False)

    print(f"execution time is {time.time() - startTime}")


entryTriggeredForRSIToSell()
