import datetime
import time
import pandas as pd

from AIlists.GetterAIList import getterAIList
from AIlists.SetterAIList import setterAIList
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from universallist.GetterUniversalList import getterUniversalList


def getAIListWithoutUdf(isLive=False):
    # startTime = time.time()
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # get universal list
        uDf = getterUniversalList()

        try:
            # getter specific nifty no
            NifNo = int(getterAIList("NiftyNo").loc[0, "NiftyNo"])
            # function for Nifty AI list
            dfBRsi = uDf.loc[uDf['id'] <= NifNo]
            setterAIList(dfBRsi, "NiftyAIList")

            # function for Buyer Rsi list (over bought region)
            dfBRsi = uDf.loc[(uDf['rsi0'] <= 40) | (uDf['rsi1'] <= 40) | (uDf['rsi2'] <= 40)]
            setterAIList(dfBRsi, "BuyerRSIAIList")

            # function for seller Rsi list (over sold region)
            dfSRsi = uDf.loc[(uDf['rsi0'] >= 80) | (uDf['rsi1'] >= 80) | (uDf['rsi2'] >= 80)]
            setterAIList(dfSRsi, "SellerRSIAIList")

            # function for bullish Reversal AI list
            dfBuRev = uDf[uDf['bulRP'].str.contains("Bullish_Engulfing|hammer|morning_star")]
            setterAIList(dfBuRev, "BullishReversalAIList")

            # function for bearish Reversal AI list
            dfBeRev = uDf[uDf['berRP'].str.contains("Bearish_Engulfing|shooting_star|evening_star")]
            setterAIList(dfBeRev, "BearishReversalAIList")
        except Exception as e:
            print(f"exception while getAIListWithoutUdf is {e}")
        time.sleep(0.125)


# getAIListWithoutUdf()
