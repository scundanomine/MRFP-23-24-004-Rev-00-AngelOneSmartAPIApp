import pandas as pd


def getterAppendAndSetterPositionList(row):
    try:
        df = pd.read_csv("F:\\AT\\position\\positionstate\\PositionList.csv")
        df.loc[len(df)] = row
        df.to_csv("F:\\AT\\position\\positionstate\\PositionList.csv", index=False)
    except Exception as e:
        print(f"The exception while getter, append and setter position List is {e}")
        getterAppendAndSetterPositionList(row)

