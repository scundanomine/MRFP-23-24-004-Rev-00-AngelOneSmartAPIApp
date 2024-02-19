import pandas as pd
from commonudm.GetterPreExitTime import getterPreExitTime


def getterDfTwoForPastThirtyCandle():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\dfTwo.csv")
    except Exception as e:
        print(f"The exception while getterDfTwoForPastThirtyCandle is {e}")
        df = getterDfTwoForPastThirtyCandle()
    return df


# print(getterAvailableMargin())
