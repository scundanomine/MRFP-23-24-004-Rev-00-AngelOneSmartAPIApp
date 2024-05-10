import pandas as pd


def getterPECBListRR():
    try:
        df = pd.read_csv(
                "F:\\AT\\readandrecord\\rrstate\\PECBList.csv")
    except Exception as e:
        print(f"The exception while getterPECBListRR is {e}")
        df = getterPECBListRR()
    return df


# print(getterPECBListRR())
