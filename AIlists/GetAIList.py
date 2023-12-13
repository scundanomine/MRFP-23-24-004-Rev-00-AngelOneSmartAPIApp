import time
from AIlists.SetterAIList import setterAIList
from universallist.GetterUniversalList import getterUniversalList


def getAIList(niftySize=300):
    startTime = time.time()

    # get universal list
    uDf = getterUniversalList()

    # function for S AI list
    def getSupportAIList():
        dfS = uDf.loc[(uDf['srT'] == "S")]
        setterAIList(dfS, "SupportAIList")
        # print(dfS)

    getSupportAIList()

    # function for R AI list
    def getResistanceAIList():
        dfR = uDf.loc[(uDf['srT'] == "R")]
        setterAIList(dfR, "ResistanceAIList")
        # print(dfR)

    getResistanceAIList()

    # function for Buyer Rsi list
    def getBuyerRSIAIList():
        dfRORI = uDf.loc[((uDf['rsi0'] >= 99) | (uDf['rsi1'] >= 99) | (uDf['rsi2'] >= 99)) & (uDf['roc0'] >= 9000)]
        setterAIList(dfRORI, "BuyerRSIAIList")
        # print(dfRORI)

    getBuyerRSIAIList()

    # function for seller Rsi list
    def getSellerRSIAIList():
        dfRORI = uDf.loc[((uDf['rsi0'] <= 1) | (uDf['rsi1'] <= 1) | (uDf['rsi2'] <= 1)) & (uDf['roc0'] <= -9000)]
        setterAIList(dfRORI, "SellerRSIAIList")
        # print(dfRORI)

    getSellerRSIAIList()

    # function for bullish Reversal AI list
    def getBullishReversalAIList():
        dfRev = uDf[uDf['bulRP'].str.contains("Bullish_Engulfing|hammer") & uDf['s'].str.contains("L|XL|2XL|GIG")]
        setterAIList(dfRev, "BullishReversalAIList")
        # print(dfRev)

    getBullishReversalAIList()

    # function for bearish Reversal AI list
    def getBearishReversalAIList():
        dfRev = uDf[uDf['berRP'].str.contains("Bearish_Engulfing|shooting_star") & uDf['s'].str.contains("L|XL|2XL|GIG")]
        setterAIList(dfRev, "BearishReversalAIList")
        # print(dfRev)

    getBearishReversalAIList()

    # function for top 10 gainer AI list
    def getTopTenGainerList(count=10):
        dfG = uDf.nlargest(count, "GL")
        setterAIList(dfG, "TopGainerList")
        # print(dfG)

    getTopTenGainerList()

    # function for top 10 loser AI list
    def getTopTenLoserList(count=10):
        dfL = uDf.nsmallest(count, "GL")
        setterAIList(dfL, "TopLoserAIList")
        # print(dfL)

    getTopTenLoserList()

    print(f"time of execution is {time.time() - startTime}")


getAIList()
