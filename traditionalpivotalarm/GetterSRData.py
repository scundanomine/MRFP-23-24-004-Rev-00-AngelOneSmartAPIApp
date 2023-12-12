import pandas as pd
from traditionalpivotalarm.SetterSRData import setterSRData


def getterSRData():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\SRData.csv")
    except Exception as e:
        print(f"The exception while getter pivot data is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = setterSRData()
    df.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    return df


# print(getterSRData())
