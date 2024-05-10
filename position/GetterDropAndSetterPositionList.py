import pandas as pd


def getterDropAndSetterPositionList(uid):
    try:
        df = pd.read_csv("F:\\AT\\position\\positionstate\\PositionList.csv")
        i = df[(df.id == uid)].index
        df = df.drop(i)
        df.to_csv("F:\\AT\\position\\positionstate\\PositionList.csv", index=False)
    except Exception as e:
        print(f"The exception while getterDropAndSetterPositionList is {e}")
        getterDropAndSetterPositionList(uid)

