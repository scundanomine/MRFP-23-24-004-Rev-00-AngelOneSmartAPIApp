import time
from AIlists.GetCustomDfGainerOrLoser import getCustomDfGainerOrLoser
from AIlists.SetterAIList import setterAIList
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from universallist.GetterUniversalList import getterUniversalList
import multiprocessing
import datetime
import pandas as pd


def getAIListWithoutUdf(isLive=False):
    startTime = time.time()
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        # get universal list
        uDf = getterUniversalList()

        # getting gainer and loser df
        glDf = getCustomDfGainerOrLoser()
    
        # function for S AI list
        dfS = uDf.loc[(uDf['srT'] == "S")]
        setterAIList(dfS, "SupportAIList")
    
        # function for R AI list
        dfR = uDf.loc[(uDf['srT'] == "R")]
        setterAIList(dfR, "ResistanceAIList")
    
        # function for Buyer Rsi list
        dfBRsi = uDf.loc[((uDf['rsi0'] >= 70) | (uDf['rsi1'] >= 70) | (uDf['rsi2'] >= 70)) & (uDf['roc0'] >= 5)]
        setterAIList(dfBRsi, "BuyerRSIAIList")
    
        # function for seller Rsi list
        dfSRsi = uDf.loc[((uDf['rsi0'] <= 30) | (uDf['rsi1'] <= 30) | (uDf['rsi2'] <= 30)) & (uDf['roc0'] <= -5)]
        setterAIList(dfSRsi, "SellerRSIAIList")
    
        # function for bullish Reversal AI list
        dfBuRev = uDf[uDf['bulRP'].str.contains("Bullish_Engulfing|hammer|tweezer_bottom|Piercing|morning_star")]
        setterAIList(dfBuRev, "BullishReversalAIList")
    
        # function for bearish Reversal AI list
        dfBeRev = uDf[uDf['berRP'].str.contains("Bearish_Engulfing|shooting_star|tweezer_top|dark_cloud_cover|evening_star")]
        setterAIList(dfBeRev, "BearishReversalAIList")
    
        # function for top 10 gainer AI list
        dfG = uDf.nlargest(glDf.loc[0, 'GL'], "GL")
        setterAIList(dfG, "TopGainerList")
    
        # function for top 10 loser AI list
        dfL = uDf.nsmallest(glDf.loc[1, 'GL'], "GL")
        setterAIList(dfL, "TopLoserAIList")
        print(f"Execution time for AI list (AI) is {time.time() - startTime}")
        time.sleep(1)


# getAIListWithoutUdf()
