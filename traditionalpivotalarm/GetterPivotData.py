import pandas as pd
from traditionalpivotalarm.SetterPrePivotData import setterPrePivotData


def getterPivotData():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\PivotData.csv")
    except Exception as e:
        print(f"The exception while getterPivotData is {e}")
        df = getterPivotData()
    return df


# print(getterPivotData())
