import pandas as pd


def getterPastTimeByMin():
    try:
        df = pd.read_csv(
            "F:\\AT\\commonudm\\resource\\PastTimeByMin.csv")
    except Exception as e:
        print(f"The exception while getter getterPastTimeByMin is {e}")
        df = getterPastTimeByMin()
    return df


# print(getterPastTimeByMin())
