import time
from AIlists.SetterAIList import setterAIList
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
from universallist.GetterUniversalList import getterUniversalList
import multiprocessing
import datetime


def getAIListWithoutUdf(lock=multiprocessing.Lock()):
    startTime = time.time()
    ctrA = 0
    lock.acquire()
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    lock.release()
    while datetime.datetime.now() - cv < exitTime:
        # get universal list
        uDf = getterUniversalList()
    
        # function for S AI list
        dfS = uDf.loc[(uDf['srT'] == "S")]
        setterAIList(lock, dfS, "SupportAIList")
    
        # function for R AI list
        dfR = uDf.loc[(uDf['srT'] == "R")]
        setterAIList(lock, dfR, "ResistanceAIList")
        # print(dfR)
    
        # function for Buyer Rsi list
        dfBRsi = uDf.loc[((uDf['rsi0'] >= 70) | (uDf['rsi1'] >= 70) | (uDf['rsi2'] >= 70)) & (uDf['roc0'] >= 10)]
        setterAIList(lock, dfBRsi, "BuyerRSIAIList")
        # print(dfBRsi)
    
        # function for seller Rsi list
        dfSRsi = uDf.loc[((uDf['rsi0'] <= 30) | (uDf['rsi1'] <= 30) | (uDf['rsi2'] <= 30)) & (uDf['roc0'] <= -10)]
        setterAIList(lock, dfSRsi, "SellerRSIAIList")
        # print(dfSRsi)
    
        # function for bullish Reversal AI list
        dfBuRev = uDf[uDf['bulRP'].str.contains("Bullish_Engulfing|hammer") & uDf['s'].str.contains("L|XL|2XL|GIG")]
        setterAIList(lock, dfBuRev, "BullishReversalAIList")
        # print(dfBuRev)
    
        # function for bearish Reversal AI list
        dfBeRev = uDf[uDf['berRP'].str.contains("Bearish_Engulfing|shooting_star") & uDf['s'].str.contains("L|XL|2XL|GIG")]
        setterAIList(lock, dfBeRev, "BearishReversalAIList")
        # print(dfBeRev)
    
        # function for top 10 gainer AI list
        dfG = uDf.nlargest(10, "GL")
        setterAIList(lock, dfG, "TopGainerList")
        # print(dfG)
    
        # function for top 10 loser AI list
        dfL = uDf.nsmallest(10, "GL")
        setterAIList(lock, dfL, "TopLoserAIList")
        # print(dfL)

        ctrA = ctrA + 1
        print(f"{ctrA} execution time for AI list is {time.time() - startTime}")
        time.sleep(5)


# getAIListWithoutUdf()
