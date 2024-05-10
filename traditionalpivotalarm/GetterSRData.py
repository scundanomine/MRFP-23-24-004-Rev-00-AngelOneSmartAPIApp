import pandas as pd
from traditionalpivotalarm.SetterSRData import setterSRData


def getterSRData():
    try:
        df = pd.read_csv(
            "F:\\AT\\traditionalpivotalarm\\pivotstate\\SRData.csv")
    except Exception as e:
        print(f"The exception while getterSRData is {e}")
        df = getterSRData()
    df.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    return df


# print(getterSRData())
