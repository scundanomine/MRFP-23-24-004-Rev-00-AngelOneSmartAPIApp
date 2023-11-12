import pandas as pd


def getNiftyDetailedListWithPivots(size):
    df = pd.read_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\NiftyDetailedListWithPivots.csv")
    dfSize = len(df)
    try:
        df = df.drop(labels=range(size, dfSize), axis=0)
    except Exception as e:
        print(f"The exception while getting getNiftyDetailedListWithPivots is {e}")
        pass
    return df


# print(getNiftyDetailedListWithPivots(300))
