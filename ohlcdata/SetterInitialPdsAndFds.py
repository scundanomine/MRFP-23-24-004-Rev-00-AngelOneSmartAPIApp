from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from ohlcdata.GetterFDS import getterFDS
from ohlcdata.GetterFFDS import getterFFDS
from ohlcdata.GetterPDS import getterPDS
from ohlcdata.GetterPastTenCandleDF import getterPastTenCandleDf
from ohlcdata.SetterFDS import setterFDS
from ohlcdata.SetterFFDS import setterFFDS
from ohlcdata.SetterPDS import setterPDS


def setterInitialPdsAndFds():
    gDf = getterRequiredSymbolAndTokenList()
    pds = getterPDS()
    fds = getterFDS()
    fFds = getterFFDS()
    for index, row in gDf.iterrows():
        uid = row['id']
        symbol = row['symbol']
        df = getterPastTenCandleDf(uid)
        data = df.iloc[9]
        pds.iloc[index] = data
        fds.iloc[index] = data
        fFds.iloc[index] = data
    setterPDS(pds)
    setterFDS(fds)
    setterFFDS(fFds)


# setterInitialPdsAndFds()
