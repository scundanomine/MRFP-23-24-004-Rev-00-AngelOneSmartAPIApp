from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET


def getterPreCustomBlackListForET():
    # get custom black list dataframe
    df = getCustomDfBlackListET()
    df.to_csv(
        "F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\CustomBlackListET.csv",
        index=False)
    # print(df)


# getterPreBlackListForET()
