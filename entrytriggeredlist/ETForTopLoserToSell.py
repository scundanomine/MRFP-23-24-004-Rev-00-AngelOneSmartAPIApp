from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForTopLoserToSell(lock):
    # get current resistance AI list
    rdf = getterAIList("TopLoserAIList")

    # getter ET black list
    bLDf = getterBlackListET()

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
            if row['rsi0'] <= 30 and row['rsi0'] < row['rsi1'] and (cTwo - cOne) <= -0.2*atr and row['roc0'] <= -10 and ("hammer" not in row["t"]):
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "ETFTopLoserForSell"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)


# entryTriggeredForTopLoserToSell()
