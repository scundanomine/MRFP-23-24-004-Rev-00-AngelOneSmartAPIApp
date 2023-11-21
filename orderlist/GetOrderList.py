from entrytriggeredlist.ETForBearishReversalPattern import entryTriggeredForBearishReversalPatternForSell
from entrytriggeredlist.ETForBullishReversalPattern import entryTriggeredForBullishReversalPatternForBuy
from entrytriggeredlist.ETForRSIToBuy import entryTriggeredForRSIToBuy
from entrytriggeredlist.ETForRSIToSell import entryTriggeredForRSIToSell
from entrytriggeredlist.ETForResistancePivot import entryTriggeredForResistancePivot
from entrytriggeredlist.ETForSupportPivot import entryTriggeredForSupportPivot
from entrytriggeredlist.ETForTopGainerToBuy import entryTriggeredForTopGainerToBuy
from entrytriggeredlist.ETForTopLoserToSell import entryTriggeredForTopLoserToSell
from entrytriggeredlist.GetBlackListForET import getBlackListForET


def getOrderList():
    # get black list for ET
    getBlackListForET()

    # OL due support and resistance
    entryTriggeredForResistancePivot()
    entryTriggeredForSupportPivot()

    # OL due to top gainer and loser
    entryTriggeredForTopGainerToBuy()
    entryTriggeredForTopLoserToSell()

    # OL due RSI
    entryTriggeredForRSIToBuy()
    entryTriggeredForRSIToSell()

    # OL due to reversal pattern
    entryTriggeredForBearishReversalPatternForSell()
    entryTriggeredForBullishReversalPatternForBuy()
