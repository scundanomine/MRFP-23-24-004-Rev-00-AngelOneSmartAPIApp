import time
from entry.GetterECBList import getterECBList
from entry.GetterEntryList import getterEntryList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
from position.GetterPositionList import getterPositionList


def getPosition():
    # getter ET list
    eTDf = getterEntryTriggeredList()

    # getter ET black list
    eTBDf = getterBlackListET()

    # getter Entry list
    eELDf = getterEntryList()

    # getter Entry calculation black list
    eCBDf = getterECBList()

    # getter position list
    pLDf = getterPositionList()

    dfItr = eELDf

    for index, row in dfItr.iterrows():
        uid = row["id"]
        ot = row["ot"]
        ltp = row["CC2"]
        lo = row['lo']
        sl = row['sl']
        refTime = row["tOEP"]
        i = eTDf[(eTDf.id == uid)].index
        # condition for long position
        if ot is "buy":
            if ltp >= lo:
                print(f"entry is place for {uid}")
                row['po'] = 'executed'
                row['tOP'] = time.time()
                # upend the list
                pLDf.iLoc[len(pLDf)] = row
                # remove specific row from Entry list
                eELDf.drop(index)
            elif ltp <= (sl + lo) / 2 or time.time() - refTime >= 600:
                row['po'] = 'cancel'
                row['sl'] = 'cancel'
                # remove specific row from Entry list
                eELDf.drop(index)
                # reset of black list
                eTBDf.loc[uid-1, "bFlag"] = False
                eCBDf.loc[uid-1, "bELFlag"] = False
                # removal of specific row from ET list
                eTDf.drop(i)
            else:
                pass

        # condition for short position
        else:
            if ltp <= lo:
                print(f"entry is place for {uid}")
                row['po'] = 'executed'
                row['tOP'] = time.time()
                # upend the list
                pLDf.iLoc[len(pLDf)] = row
                # remove specific row from Entry list
                eELDf.drop(index)
            elif ltp >= (sl + lo) / 2 or time.time() - refTime >= 600:
                row['po'] = 'cancel'
                row['sl'] = 'cancel'
                # remove specific row from Entry list
                eELDf.drop(index)
                # reset of black list
                eTBDf.loc[uid-1, "bFlag"] = False
                eCBDf.loc[uid-1, "bELFlag"] = False
                # removal of specific row from ET list
                eTDf.drop(i)
            else:
                pass

    # setter for eTDf
