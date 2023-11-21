import pandas as pd


def getterBlackListET():
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv")
    except Exception as e:
        print(f"The exception while getter ET black list is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\SymbolAndToken.csv")
        df = df.loc[:, ['id']]
        df['bFlag'] = False
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv",
            index=False)
    return df


# getterBlackListET()
