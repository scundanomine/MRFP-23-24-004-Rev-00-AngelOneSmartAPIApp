import pandas as pd


def getterBlackListET():
    try:
        df = pd.read_csv(
            f"F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv")
    except Exception as e:
        print(f"The exception while getterBlackListET is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterBlackListET()
    return df


# getterBlackListET()
