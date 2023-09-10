import pandas as pd


def saveSRN(df):
    df.to_csv("srn.csv", index=False)
    print(df)


def readSRN():
    rft = pd.read_csv("srn.csv", sep=',', skipinitialspace=True)
    rft.columns = rft.iloc[0]
    rft = rft[1:]
    rft.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    rft[0] = rft[0].astype("int64")
    return rft
