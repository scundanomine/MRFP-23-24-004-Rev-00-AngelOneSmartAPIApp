from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
from entrytriggeredlist.CheckBearishReversalCandle import checkBearishReversalCandle
from entrytriggeredlist.CheckBullishReversalPattern import checkBullishReversalPattern


def checkBullishMarket():
    df = getterSpecificCandleData(120, "Nifty 50")
    cOne = df.loc[8, 'C']
    cTwo = df.loc[9, 'C']
    atr = df.loc[9, 'atr']
    if df.loc[9, 'sma'] < cTwo:
        return True
    elif cTwo > cOne and checkBullishReversalPattern(df.loc[8, "bulRP"]) and df.loc[9, 'g'] == 'green' and df.loc[9, 'roc'] <= -15 and not checkBearishReversalCandle(df.loc[9, "t"]):
        return True
    elif df.loc[9, 'rsi'] > df.loc[8, 'rsi'] > df.loc[7, 'rsi'] and (cTwo - cOne) >= 0.2*atr and df.loc[9, 'roc'] <= -15 and not checkBearishReversalCandle(df.loc[9, "t"]):
        return True
    else:
        return False
    