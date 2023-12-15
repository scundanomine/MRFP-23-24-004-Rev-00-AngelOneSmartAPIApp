import pandas as pd

from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET


def getterBlackListET(lock):
    try:
        lock.aquire()
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv")
        lock.release()
    except Exception as e:
        print(f"The exception while getter ET black list is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getCustomDfBlackListET(lock)
    return df


# getterBlackListET()
