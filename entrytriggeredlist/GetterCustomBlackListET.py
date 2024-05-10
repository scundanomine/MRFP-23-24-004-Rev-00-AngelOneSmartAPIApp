import pandas as pd


def getterCustomBlackListET():
    try:
        df = pd.read_csv(
            "F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\CustomBlackListET.csv")
    except Exception as e:
        print(f"The exception while getterCustomBlackListET is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterCustomBlackListET()
    return df


# getterBlackListET()
