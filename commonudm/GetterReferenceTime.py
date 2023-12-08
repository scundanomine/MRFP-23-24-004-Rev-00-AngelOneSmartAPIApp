import pandas as pd
from commonudm.GetterPreReferenceTime import getterPreReferenceTime


def getterReferenceTime():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\RefTime.csv")
    except Exception as e:
        print(f"The exception while Reference Time is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterPreReferenceTime()
    # return df['refTime'][0]
    return df['refTime'][0]


# print(getterAvailableMargin())
