from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from eventloop.CreateGSTDataFile import createGSTDataFile


def cleaningAndSettingGSTDataFiles():
    gDf = getterRequiredSymbolAndTokenList()
    for index, row in gDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        createGSTDataFile(uid, symbol)


# cleaningAndSettingGSTDataFiles()
