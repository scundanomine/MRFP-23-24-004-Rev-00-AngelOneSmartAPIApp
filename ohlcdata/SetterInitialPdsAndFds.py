from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from ohlcdata.GetterFDS import getterFDS
from ohlcdata.GetterPDS import getterPDS
from ohlcdata.GetterPastTenCandleDF import getterPastTenCandleDf
from ohlcdata.SetterFDS import setterFDS
from ohlcdata.SetterPDS import setterPDS


def setterInitialPdsAndFds():
    gDf = getterRequiredSymbolAndTokenList()
    pds = getterPDS()
    fds = getterFDS()
    for index, row in gDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        df = getterPastTenCandleDf(uid, symbol)
        pds.iloc[index] = df.iloc[9]
        fds.iloc[index] = df.iloc[9]
    setterPDS(pds)
    setterFDS(fds)


# setterInitialPdsAndFds()
