import pandas as pd


def setterPrePECBListRR():
    # flag for entry calculation
    df = pd.DataFrame(columns=['pid', 'flagCP', 'flagCE'])
    df.to_csv(
        "F:\\AT\\readandrecord\\rrstate\\PECBList.csv",
        index=False)
    return df


# print(setterPrePECBListRR())
