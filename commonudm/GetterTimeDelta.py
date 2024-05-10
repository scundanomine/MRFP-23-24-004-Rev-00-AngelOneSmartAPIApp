import pandas as pd


def getterTimeDelta():
    try:
        df = pd.read_csv(
            "F:\\AT\\commonudm\\resource\\TimeDelta.csv")
    except Exception as e:
        print(f"The exception while getter timeDelta is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterTimeDelta()
    # return df['exitTime'][0]
    c = pd.to_timedelta(df['timeDelta'][0])
    return c


# print(getterTimeDelta())
