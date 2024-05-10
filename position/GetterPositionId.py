import pandas as pd
import multiprocessing


def getterPositionId():
    try:
        df = pd.read_csv(
            "F:\\AT\\position\\positionstate\\PId.csv")
        sid = df.loc[0, 'pid']
    except Exception as e:
        print(f"The exception while getterPositionId is {e}")
        sid = getterPositionId()
    return sid


# print(getterPositionId())
