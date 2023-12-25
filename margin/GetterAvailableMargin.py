import pandas as pd
from margin.GetterPreMargin import getterPreMargin


def getterAvailableMargin():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv")
    except Exception as e:
        print(f"The exception while getter margin is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterPreMargin()
    # return df['margin'][0]
    return df


# print(getterAvailableMargin())
