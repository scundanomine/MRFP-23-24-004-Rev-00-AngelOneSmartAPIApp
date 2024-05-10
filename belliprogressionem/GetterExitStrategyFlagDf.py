import pandas as pd


def getterExitStrategyFlagDf():
    try:
        df = pd.read_csv("F:\\AT\\belliprogressionem\\state\\ExSFlag.csv")
    except Exception as e:
        print(f"The exception while getterExitStrategyFlagDf is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitStrategyFlagDf()
    return df


# print(getterExitStrategyFlag())
