import pandas as pd
from readandrecord.SetterPrePECBListRR import setterPrePECBListRR


def getterPECBListRR():
    try:
        df = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\PECBList.csv")
    except Exception as e:
        print(f"The exception while getterPECBListRR is {e}")
        df = setterPrePECBListRR()
    return df


# print(getterPECBListRR())
