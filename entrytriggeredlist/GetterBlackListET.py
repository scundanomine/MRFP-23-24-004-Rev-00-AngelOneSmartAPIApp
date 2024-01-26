import pandas as pd


def getterBlackListET():
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv")
    except Exception as e:
        print(f"The exception while getterBlackListET is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterBlackListET()
    return df


# getterBlackListET()
