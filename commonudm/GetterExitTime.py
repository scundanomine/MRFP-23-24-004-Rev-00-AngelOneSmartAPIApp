import pandas as pd
from commonudm.GetterPreExitTime import getterPreExitTime


def getterExitTime():
    try:
        df = pd.read_csv(
            "F:\\AT\\commonudm\\resource\\ExitTime.csv")
    except Exception as e:
        print(f"The exception while Exit Time is {e}")
        df = getterPreExitTime()
    # return df['exitTime'][0]
    return pd.to_datetime(df['exitTime'][0])


# print(getterAvailableMargin())
