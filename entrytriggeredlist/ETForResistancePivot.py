import multiprocessing

from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterCustomBlackListET import getterCustomBlackListET
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForResistancePivot(lock=multiprocessing.Lock()):
    # get current resistance AI list
    rdf = getterAIList("ResistanceAIList")

    # getter ET black list
    bLDf = getterBlackListET()
    cBLDf = getterCustomBlackListET()

    for index, row in rdf.iterrows():
        uid = row['id']
        # condition of black listed
        if bLDf['bFlag'][uid - 1] == 1 or cBLDf['bFlag'][uid - 1] == 1:
            continue
        else:
            cOne = row['CC1']
            cTwo = row['CC2']
            rV = row['srV']
            atr = row['atr']
            # condition for buy
            if cTwo >= rV and cOne >= rV and (cTwo - cOne) >= 0.25 * atr and row['rsi0'] >= 60 and not (checkBearishReversalPattern(row["berRPC"])):
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "ETFResistancePivotToBuy"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)

            # condition for 'sell'
            elif cTwo <= rV and cOne <= rV and (cTwo - cOne) <= -0.25 * atr and checkBearishReversalPattern(
                    row["berRP"]) and ("hammer" not in row["t"]):
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "ETFResistancePivotToSell"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)

# entryTriggeredForResistancePivot()
