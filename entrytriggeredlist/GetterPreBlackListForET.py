from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET
from entrytriggeredlist.GetterBlackListET import getterBlackListET


def getterPreBlackListForET():
    # get custom black list dataframe
    df = getCustomDfBlackListET()
    df["bFlag"] = 0
    df.to_csv(
        "F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv",
        index=False)
    # print(df)


# getterPreBlackListForET()
