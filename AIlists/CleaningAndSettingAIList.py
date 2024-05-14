from AIlists.SetterAIList import setterAIList
from AIlists.SetterPreNiftyNo import setterPreNiftyNo
from universallist.GetterUniversalList import getterUniversalList
import multiprocessing


def cleaningAndSettingAIList(lock=multiprocessing.Lock()):
    uDf = getterUniversalList()
    setterPreNiftyNo()

    # function for S AI list
    dfS = uDf.loc[(uDf['srT'] == "P")]
    setterAIList(dfS, "BuyerRSIAIList")
    setterAIList(dfS, "SellerRSIAIList")
    setterAIList(dfS, "BullishReversalAIList")
    setterAIList(dfS, "BearishReversalAIList")
    setterAIList(dfS, "NiftyAIList")


# cleaningAndSettingAIList()
