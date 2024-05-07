import pandas as pd


def getterExitStrategyFlag():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\belliprogressionem\\state\\ExSFlag.csv")
    except Exception as e:
        print(f"The exception while getterExitStrategyFlag is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitStrategyFlag()
    return df.loc[0, "xBF"], df.loc[0, "xSF"]


# print(getterETStrategyFlag())
