import pandas as pd
from commonudm.GetterPreExitTime import getterPreExitTime


def getterExitTime():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\ExitTime.csv")
    except Exception as e:
        print(f"The exception while Exit Time is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterPreExitTime()
    # return df['exitTime'][0]
    return pd.to_datetime(df['exitTime'][0])


# print(getterAvailableMargin())
