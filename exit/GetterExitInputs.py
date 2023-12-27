import pandas as pd
from exit.GetCustomDfExitInputs import getCustomDfExitInputs


def getterExitInputs(lock):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv")
    except Exception as e:
        print(f"The exception while getter Exit inputs is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getCustomDfExitInputs(lock)
    return df


# getterBlackListET()
