from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET


def getterPreCustomBlackListForET():
    # get custom black list dataframe
    df = getCustomDfBlackListET()
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\CustomBlackListET.csv",
        index=False)
    # print(df)


# getterPreBlackListForET()
