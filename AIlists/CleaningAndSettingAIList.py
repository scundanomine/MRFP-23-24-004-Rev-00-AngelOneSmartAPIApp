from AIlists.SetterAIList import setterAIList
from universallist.GetterUniversalList import getterUniversalList
import multiprocessing


def cleaningAndSettingAIList(lock=multiprocessing.Lock()):
    uDf = getterUniversalList()

    # function for S AI list
    dfS = uDf.loc[(uDf['srT'] == "P")]
    setterAIList(lock, dfS, "SupportAIList")
    setterAIList(lock, dfS, "ResistanceAIList")
    setterAIList(lock, dfS, "BuyerRSIAIList")
    setterAIList(lock, dfS, "SellerRSIAIList")
    setterAIList(lock, dfS, "BullishReversalAIList")
    setterAIList(lock, dfS, "BearishReversalAIList")
    setterAIList(lock, dfS, "TopGainerList")
    setterAIList(lock, dfS, "TopLoserAIList")


# cleaningAndSettingAIList()
