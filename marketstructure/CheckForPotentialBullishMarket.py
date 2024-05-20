from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from entrytriggeredlist.CheckBearishReversalCandle import checkBearishReversalCandle
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern


def checkForPotentialBullishMarket():
    df = getterSpecificCandleData(120, "Nifty 50")
    # if df.loc[9, 'sma'] < df.loc[9, 'C'] and df.loc[8, 'sma'] < df.loc[8, 'C'] and df.loc[7, 'sma'] < df.loc[7, 'C'] and df.loc[6, 'sma'] < df.loc[6, 'C'] and df.loc[5, 'sma'] < df.loc[5, 'C']:
    if df.loc[9, 'sma'] < df.loc[9, 'C'] and df.loc[8, 'sma'] < df.loc[8, 'C'] and df.loc[7, 'sma'] < df.loc[7, 'C']:
        return True
    else:
        return False
    