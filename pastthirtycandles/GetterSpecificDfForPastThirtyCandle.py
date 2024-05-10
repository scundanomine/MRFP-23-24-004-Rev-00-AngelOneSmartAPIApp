import pandas as pd
from commonudm.GetterPreExitTime import getterPreExitTime


def getterSpecificDfForPastThirtyCandle(fileName):
    try:
        df = pd.read_csv(
            f"F:\\AT\\pastthirtycandles\\pastthirycandlesstate\\{fileName}.csv")
    except Exception as e:
        print(f"The exception while getterSpecificDfForPastThirtyCandle is {e}")
        df = getterSpecificDfForPastThirtyCandle(fileName)
    return df


# print(getterAvailableMargin())
