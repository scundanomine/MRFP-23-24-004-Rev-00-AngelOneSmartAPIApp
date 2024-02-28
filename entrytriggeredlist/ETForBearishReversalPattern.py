from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBullishReversalCandle import checkBullishReversalCandle
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForBearishReversalPatternForSell(lock):
    # get current resistance AI list
    rdf = getterAIList("BearishReversalAIList")

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
            # atr = row['atr']
            rsi = row['rsi0']

            # condition for 'sell'
            if cTwo < cOne and checkBearishReversalPattern(row["berRP"]) and row['g'] == 'red' and row['roc0'] >= 15 and not checkBullishReversalCandle(row["t"]):
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "ETFBearishReversalPatternToSell"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)


# entryTriggeredForBearishReversalPatternForSell()
