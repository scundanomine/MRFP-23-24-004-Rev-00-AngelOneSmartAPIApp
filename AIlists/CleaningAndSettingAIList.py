from AIlists.SetterAIList import setterAIList
from universallist.GetterUniversalList import getterUniversalList
import multiprocessing


def cleaningAndSettingAIList(lock=multiprocessing.Lock()):
    uDf = getterUniversalList()

    # function for S AI list
    dfS = uDf.loc[(uDf['srT'] == "P")]
    setterAIList(dfS, "SupportAIList")
    setterAIList(dfS, "ResistanceAIList")
    setterAIList(dfS, "BuyerRSIAIList")
    setterAIList(dfS, "SellerRSIAIList")
    setterAIList(dfS, "BullishReversalAIList")
    setterAIList(dfS, "BearishReversalAIList")
    setterAIList(dfS, "TopGainerList")
    setterAIList(dfS, "TopLoserAIList")


# cleaningAndSettingAIList()
