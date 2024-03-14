from entry.GetterUpdateAndSetterECBList import getterUpdateAndSetterECBList
from entrytriggeredlist.GetterDropAndSetterEntryTriggeredList import getterDropAndSetterEntryTriggeredList
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET
from exit.GetterUpdateAndSetterExitInputs import getterUpdateAndSetterExitInputs
from margin.GetterCreditAndSetterAvailableMargin import getterCreditAndSetterAvailableMargin
from portfolio.GetterCurrentPortfolio import getterCurrentPortfolio
from portfolio.GetterUpdateAndSetterFixedPortfolio import getterUpdateAndSetterFixedPortfolio
from position.GetterDropAndSetterPositionList import getterDropAndSetterPositionList
from readandrecord.SetExitDetailsAndCandles import setExitDetailsAndCandles


def exitUDf(pid, uid, symbol, row, cv, reportDate, mr, gol, lock):
    with lock:
        # remove specific row from Entry list
        getterDropAndSetterPositionList(uid)
        # reset of black list
        getterUpdateAndSetterBlackListET(uid, 0)
        getterUpdateAndSetterECBList(uid, 0)
        # removal of specific row from ET list
        getterDropAndSetterEntryTriggeredList(uid)
    getterUpdateAndSetterExitInputs([uid, 0, 0], lock)
    getterCreditAndSetterAvailableMargin(mr, lock)
    getterUpdateAndSetterFixedPortfolio(gol, lock)
    row['tOEP'] = getterCurrentPortfolio()
    # read and record for exit
    setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate)
