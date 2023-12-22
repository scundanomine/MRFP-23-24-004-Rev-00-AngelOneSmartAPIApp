from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET
from entrytriggeredlist.GetterBlackListET import getterBlackListET


def getBlackListForET(lock):
    # get custom black list dataframe
    df = getCustomDfBlackListET(lock)

    # getter black list
    bLDf = getterBlackListET(lock)

    for index, row in df.iterrows():
        if row["bFlag"]:
            bLDf.iloc[index] = row['bFlag']
    lock.acquire()
    bLDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv",
        index=False)
    lock.release()

    # print(bLDf)

# getBlackListForET()
