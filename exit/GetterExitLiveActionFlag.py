import pandas as pd


def getterExitLiveActionFlag():
    try:
        df = pd.read_csv(
            "F:\\AT\\exit\\exitstate\\EXLAFlag.csv")
    except Exception as e:
        print(f"The exception while getterETLiveActionFlag is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitLiveActionFlag()
    return df.loc[0, "eXBF"], df.loc[0, "eXSF"]


# print(getterETLiveActionFlag())
