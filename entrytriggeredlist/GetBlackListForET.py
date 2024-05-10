from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET
from entrytriggeredlist.GetterBlackListET import getterBlackListET
import multiprocessing

from entrytriggeredlist.GetterCustomBlackListET import getterCustomBlackListET


def getBlackListForET(lock=multiprocessing.Lock()):
    # get custom black list dataframe
    with lock:
        df = getCustomDfBlackListET()

    # getter black list
    bLDf = getterBlackListET()

    for index, row in df.iterrows():
        if row["bFlag"] == 1:
            bLDf.loc[index, 'bFlag'] = row['bFlag']
    bLDf.to_csv(
        "F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv",
        index=False)


# getBlackListForET()
