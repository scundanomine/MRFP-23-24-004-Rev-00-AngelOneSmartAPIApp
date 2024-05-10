import pandas as pd


def getterETLiveActionFlag():

    try:
        df = pd.read_csv(
            "F:\\AT\\entry\\entrystate\\ETLAFlag.csv")
    except Exception as e:
        print(f"The exception while getterETLiveActionFlag is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterETLiveActionFlag()
    return df.loc[0, "eTBF"], df.loc[0, "eTSF"]


# print(getterETLiveActionFlag())
