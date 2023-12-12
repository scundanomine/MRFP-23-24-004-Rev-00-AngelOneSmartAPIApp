import pandas as pd
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData


def getterPivotData():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\PivotData.csv")
    except Exception as e:
        print(f"The exception while getter pivot data is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = setterPrePivotData()
    return df


# print(getterPivotData())
