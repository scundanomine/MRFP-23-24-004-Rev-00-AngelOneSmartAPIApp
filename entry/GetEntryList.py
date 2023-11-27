from entry.GetterECBList import getterECBList
from entry.GetterEntryList import getterEntryList
from entry.LongPositionCalculator import longPositionCalculator
from entry.ShortPositionCalculator import shortPositionCalculator
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList
import datetime
from margin.GetterAvailableMargin import getterAvailableMargin
from margin.SetterAvailableMargin import setterAvailableMargin


def getEntryList():
    # Getter for entry list
    eLDf = getterEntryList()

    # getter Entry calculated and entry happened black list
    eCBLDf = getterECBList()

    # getter ET list
    eTDf = getterEntryTriggeredList()

    for index, row in eTDf.iterrows():
        uid = row['id']
        ltp = row['CC2']
        atr = row['atr']
        margin = 5
        ot = row['ot']
        if eCBLDf['eCBFlag'][uid-1]:
            continue
        else:
            if ot == 'buy':
                q, sl, target = longPositionCalculator(ltp, atr, 500, 1.2, 50000, margin, 1.5)
            else:
                q, sl, target = shortPositionCalculator(ltp, atr, 500, 1.2, 50000, margin, 1.5)
            # calculation for margin required
            mr = 1.01*ltp*q/margin
            maDf = getterAvailableMargin()
            ma = maDf['margin'][0]
            if mr <= ma:
                upList = [uid, ot, ltp, 1.01*ltp, q, sl, target, mr, 'open', 'open', '', datetime.datetime.now()]
                eLDf.loc[len(eLDf)] = upList
                eCBLDf['eCBFlag'][uid - 1] = True
                maDf.loc[0, 'margin'] = ma - mr
                setterAvailableMargin(maDf)
            else:
                pass
    # setter for ET black list
    eCBLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)

    # setter for Entry Triggered list
    eLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv", index=False)
