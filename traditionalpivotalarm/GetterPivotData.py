import pandas as pd
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData


def getterPivotData():
    try:
        df = pd.read_csv(
            "F:\\AT\\traditionalpivotalarm\\pivotstate\\PivotData.csv")
    except Exception as e:
        print(f"The exception while getterPivotData is {e}")
        df = getterPivotData()
    return df


# print(getterPivotData())
