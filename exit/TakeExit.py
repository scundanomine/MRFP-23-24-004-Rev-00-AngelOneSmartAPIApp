import time
from entry.GetterECBList import getterECBList
from entry.GetterEntryList import getterEntryList
from entry.SetterECBList import setterECBList
from entry.SetterEntryList import setterEntryList
from entrytriggeredlist.GetterBlackListET import getterBlackListET
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
from entrytriggeredlist.SetterBlackListET import setterBlackListET
from entrytriggeredlist.SetterEntryTriggeredList import setterEntryTriggeredList
from position.GetterPositionList import getterPositionList
from position.SetterPositionList import setterPositionList


def takeExit():
    # getter ET list
    eTDf = getterEntryTriggeredList()

    # getter ET black list
    eTBDf = getterBlackListET()

    # getter Entry calculation black list
    eCBDf = getterECBList()

    # getter position list
    pLDf = getterPositionList()

    dfItr = pLDf

    for index, row in dfItr.iterrows():
        uid = row["id"]
        ot = row["ot"]
        ltp = row["CC2"]
        lo = row['lo']
        sl = row['sl']
        target = row['target']
        refTime = row["tOP"]
        q = row['q']
        rowC = eTDf.loc[(eTDf['id'] == uid)]
        rsi = rowC['rsi0']
        rsiP = rowC['rsi1']
        roc = rowC['roc0']
        atr = rowC['atr']
        if ot is "buy":
            # condition for riding
            if ltp >= 0.8 * target or (rsi >= 70 and rsi >= rsiP):
                eTDf.loc[(eTDf['id'] == uid)]['sl'] = ltp - 1.5 * atr
                eTDf.loc[(eTDf['id'] == uid)]['target'] = ltp + 1.2*1.5 * atr
            # condition for exit
            elif ltp >= target or time.time()-refTime >= 1800:
                pass
                
