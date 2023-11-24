from entry.GetterECBList import getterECBList
from entry.GetterEntryList import getterEntryList
from entry.LongPositionCalculator import longPositionCalculator
from entry.ShortPositionCalculator import shortPositionCalculator
from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList


def getEntryList():
    # Getter for entry list
    eLDf = getterEntryList()

    # getter Entry calculated and entry happened black list
    eCBLDf = getterECBList()

    # getter ET list
    eTDf = getterEntryTriggeredList()

    for index, row in eTDf.iterrows():
        uid = row['id']
        if eCBLDf['eCBFlag'][uid-1]:
            continue
        else:
            if row['ot'] == 'buy':
                q, sl, target = longPositionCalculator(row['CC2'], row['atr'], 500, 1.2, 50000, 5, 1.5)
            else:
                q, sl, target = shortPositionCalculator(row['CC2'], row['atr'], 500, 1.2, 50000, 5, 1.5)
            upList = [uid, row['CC2'], 1.01*row['CC2'], q, sl, target]
            eTDf.loc[len(eTDf)] = upList
            eCBLDf['eCBFlag'][uid - 1] = True

    # setter for ET black list
    eCBLDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)

    # setter for Entry Triggered list
    eTDf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv", index=False)




