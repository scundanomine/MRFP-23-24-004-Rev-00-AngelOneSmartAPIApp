import pandas as pd


def getterExitStrategyFlagDf():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\belliprogressionem\\state\\ExSFlag.csv")
    except Exception as e:
        print(f"The exception while getterExitStrategyFlagDf is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitStrategyFlagDf()
    return df


# print(getterExitStrategyFlag())
