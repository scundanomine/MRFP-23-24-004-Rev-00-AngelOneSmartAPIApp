import time
import pandas as pd


def recursionResearch():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat2.csv")
    except Exception as e:
        print(f"The exception while recursionResearch is {e}")
        time.sleep(1)
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = recursionResearch()

    return df


print(recursionResearch())
