from AIlists.SetterAIList import setterAIList
from entrytriggeredlist.SetterEntryTriggeredList import setterEntryTriggeredList
from universallist.GetterUniversalList import getterUniversalList
import multiprocessing


def cleaningAndSettingETList(lock=multiprocessing.Lock()):
    uDf = getterUniversalList()

    # function for S AI list
    dfS = uDf.loc[(uDf['srT'] == "P")]
    setterEntryTriggeredList(dfS)


# cleaningAndSettingETList()
