import pandas as pd


def getterExitLiveActionFlagDf():
    try:
        df = pd.read_csv(
            "F:\\AT\\exit\\exitstate\\EXLAFlag.csv")
    except Exception as e:
        print(f"The exception while getterExitLiveActionFlagDf is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitLiveActionFlagDf()
    return df


# print(getterETLiveActionFlag())
