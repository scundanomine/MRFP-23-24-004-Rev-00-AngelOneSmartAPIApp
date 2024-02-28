from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
import multiprocessing
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForTopGainerToBuy(lock=multiprocessing.Lock()):
    # get current resistance AI list
    rdf = getterAIList("TopGainerList")

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
            if row['rsi0'] >= 70 and row['rsi0'] > row['rsi1'] and (cTwo - cOne) >= 0.2*atr and row['roc0'] >= 10 and ("shooting_star" not in row["t"]):
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "ETFTopGainerForBuy"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)


# entryTriggeredForTopGainerToBuy()
