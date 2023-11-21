from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET
from entrytriggeredlist.GetterBlackListET import getterBlackListET


def getUpperBoundForBlackListET(param):
    pass


def getBlackListForET():
    # get custom black list dataframe
    df = getCustomDfBlackListET("BlackList")

    # getter black list
    bLDf = getterBlackListET()

    for index, row in df.iterrows():
        uid = row["id"]
        bLDf.loc[uid - 1, 'bFlag'] = row['bFlag']

        # setter Black list
        # setter for ET black list
        bLDf.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv",
            index=False)

    print(bLDf)


# getBlackListForET()
