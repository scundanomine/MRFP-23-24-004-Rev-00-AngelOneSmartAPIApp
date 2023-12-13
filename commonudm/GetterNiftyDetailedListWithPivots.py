import pandas as pd
from commonudm.SetterNiftyDetailedListWithPivots import setterNiftyDetailedListWithPivot


def getterNiftyDetailedListWithPivots():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\NiftyDetailedListWithPivots.csv")
    except Exception as e:
        print(f"the exception while getter NiftyDetailedListWithPivots is {e} ")
        df = setterNiftyDetailedListWithPivot()
    return df


# print(getNiftyDetailedListWithPivots(300))
