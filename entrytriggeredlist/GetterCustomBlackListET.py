import pandas as pd


def getterCustomBlackListET():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\CustomBlackListET.csv")
    except Exception as e:
        print(f"The exception while getterCustomBlackListET is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterCustomBlackListET()
    return df


# getterBlackListET()
