from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBearishReversalCandle import checkBearishReversalCandle
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET
import multiprocessing


def entryTriggeredForBullishReversalPatternForBuy(flagBearish, lock=multiprocessing.Lock()):
    # get current resistance AI list
    rdf = getterAIList("BullishReversalAIList")

    # getter ET black list
    bLDf = getterBlackListET()

    for index, row in rdf.iterrows():
        uid = row['id']
        # condition of black listed
        if bLDf['bFlag'][uid - 1] == 1:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            # atr = row['atr']
            rsi = row['rsi0']

            # condition for buy
            if not flagBearish and cTwo > cOne and checkBullishReversalPattern(row["bulRP"]) and row['g'] == 'green' and row['roc0'] <= -15 and not checkBearishReversalCandle(row["t"]):
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "ETFBullishReversalPatternToBuy"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)


# entryTriggeredForBullishReversalPatternForBuy()
