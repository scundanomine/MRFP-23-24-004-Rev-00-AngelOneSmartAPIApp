import pandas as pd


def getterExitStrategyFlag():
    try:
        df = pd.read_csv("F:\\AT\\belliprogressionem\\state\\ExSFlag.csv")
    except Exception as e:
        print(f"The exception while getterExitStrategyFlag is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitStrategyFlag()
    return df.loc[0, "xBF"], df.loc[0, "xSF"]


# print(getterExitStrategyFlag())
