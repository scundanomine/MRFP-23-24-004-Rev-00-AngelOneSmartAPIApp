import pandas as pd
from commonudm.GetterPreExitTime import getterPreExitTime


def getterDfOneForPastThirtyCandle():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\dfOne.csv")
    except Exception as e:
        print(f"The exception while getterDfOneForPastThirtyCandle is {e}")
        df = getterDfOneForPastThirtyCandle()
    return df


# print(getterAvailableMargin())
