import time
from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.BlackListET import getterBlackListET
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from orderlist.GetterOrderList import getterOrderList


def entryTriggeredForSupportPivot(niftySize=300):
    startTime = time.time()

    # get current resistance AI list
    rdf = getterAIList("SupportAIList")
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
            rV = row['srV']
            atr = row['atr']
            # condition for breakout or sell
            if cTwo <= rV and cOne <= rV and (cTwo - cOne) <= -0.25*atr and row['rsi'] <= 40:
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "EntryTriggeredDueToSupportPivot"
                oLDf.loc[len(oLDf)] = row
                # update the black list
                bLDf.loc[uid+1, 'bFlag'] = True

            # condition for sell
            elif cTwo >= rV and cOne >= rV and (cTwo - cOne) >= 0.25*atr and checkBullishReversalPattern(row["bulRP"]):
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "EntryTriggeredDueToSupportPivot"
                oLDf.loc[len(oLDf)] = row
                # update the black list
                bLDf.loc[uid + 1, 'bFlag'] = True

            # condition for no buy or sale
            else:
                pass

    # setter for ET black list
    bLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)

    # setter for Order list black list
    oLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\orderlist\\olstate\\OrderList.csv", index=False)

    print(f"execution time is {time.time() - startTime}")


entryTriggeredForSupportPivot()
