from entrytriggeredlist.ETForBearishReversalPattern import entryTriggeredForBearishReversalPatternForSell
from entrytriggeredlist.ETForBullishReversalPattern import entryTriggeredForBullishReversalPatternForBuy
from entrytriggeredlist.ETForRSIToBuy import entryTriggeredForRSIToBuy
from entrytriggeredlist.ETForRSIToSell import entryTriggeredForRSIToSell
from entrytriggeredlist.ETForResistancePivot import entryTriggeredForResistancePivot
from entrytriggeredlist.ETForSupportPivot import entryTriggeredForSupportPivot
from entrytriggeredlist.ETForTopGainerToBuy import entryTriggeredForTopGainerToBuy
from entrytriggeredlist.ETForTopLoserToSell import entryTriggeredForTopLoserToSell
from entrytriggeredlist.GetBlackListForET import getBlackListForET


def getEntryTriggeredList():
    # get black list for ET
    getBlackListForET()

    # EL due support and resistance
    entryTriggeredForResistancePivot()
    entryTriggeredForSupportPivot()

    # EL due to top gainer and loser
    entryTriggeredForTopGainerToBuy()
    entryTriggeredForTopLoserToSell()

    # EL due RSI
    entryTriggeredForRSIToBuy()
    entryTriggeredForRSIToSell()

    # EL due to reversal pattern
    entryTriggeredForBearishReversalPatternForSell()
    entryTriggeredForBullishReversalPatternForBuy()
