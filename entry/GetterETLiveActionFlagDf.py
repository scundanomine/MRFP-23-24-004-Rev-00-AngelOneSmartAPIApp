import pandas as pd


def getterETLiveActionFlagDf():

    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ETLAFlag.csv")
    except Exception as e:
        print(f"The exception while getterETLiveActionFlagDf is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterETLiveActionFlagDf()
    # return df.loc[0, "eTBF"], df.loc[0, "eTSF"]
    return df


# print(getterETLiveActionFlag())
