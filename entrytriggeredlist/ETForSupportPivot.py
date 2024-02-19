from AIlists.GetterAIList import getterAIList
from entrytriggeredlist.CheckBearishReversalPattern import checkBearishReversalPattern
from entrytriggeredlist.GetterAppendAndSetterEntryTriggeredList import getterAppendAndSetterEntryTriggeredList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern
import multiprocessing
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def entryTriggeredForSupportPivot(lock=multiprocessing.Lock()):
    # get current resistance AI list
    rdf = getterAIList("SupportAIList")

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
            rV = row['srV']
            atr = row['atr']
            # condition for breakout or sell
            if cTwo <= rV and cOne <= rV and (cTwo - cOne) <= -0.25*atr and row['rsi0'] <= 40 and ("hammer" not in row["bulRPC"]):
                # update the order type and upend the order list
                row["ot"] = "sell"
                row['oc'] = "ETFSupportPivotToSell"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)

            # condition for buy
            elif cTwo >= rV and cOne >= rV and (cTwo - cOne) >= 0.25*atr and checkBullishReversalPattern(row["bulRP"]) and ("shooting_star" not in row["berRPC"]):
                # update the order type and upend the order list
                row["ot"] = "buy"
                row['oc'] = "ETFSupportPivotToBuy"
                with lock:
                    getterAppendAndSetterEntryTriggeredList(row)
                    # update the black list
                    getterUpdateAndSetterBlackListET(uid, 1)


# entryTriggeredForSupportPivot()
