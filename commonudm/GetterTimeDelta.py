import pandas as pd
from commonudm.GetterPreTimeDelta import getterPreTimeDelta


def getterTimeDelta():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\TimeDelta.csv")
    except Exception as e:
        print(f"The exception while getter timeDelta is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterPreTimeDelta()
    # return df['exitTime'][0]
    c = pd.to_timedelta(df['timeDelta'][0])
    return c


# print(getterTimeDelta())
