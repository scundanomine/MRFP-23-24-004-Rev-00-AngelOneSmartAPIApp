import pandas as pd


def getterETStrategyFlag():
    try:
        df = pd.read_csv("F:\\AT\\belliprogressionem\\state\\ETSFlag.csv")
    except Exception as e:
        print(f"The exception while getterETStrategyFlag is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterETStrategyFlag()
    return df.loc[0, "eTBF"], df.loc[0, "eTSF"]


# print(getterETStrategyFlag())
