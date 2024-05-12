import pandas as pd


def getterExitLiveActionFlagDf():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\EXLAFlag.csv")
    except Exception as e:
        print(f"The exception while getterExitLiveActionFlagDf is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitLiveActionFlagDf()
    return df


# print(getterETLiveActionFlag())
