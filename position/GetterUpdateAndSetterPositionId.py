import multiprocessing
import pandas as pd

from position.GetterPositionIdForSpecificDate import getterPositionIdForSpecificDate


def getterUpdateAndSetterPositionId(rDate, lock=multiprocessing.Lock()):
    try:
        with lock:
            pid = getterPositionIdForSpecificDate(rDate)
            pid = pid + 1
            df = pd.DataFrame([pid], columns=['pid'])
            df.to_csv(
                    f"F:\\AT\\report\\media\\{rDate}\\state\\PId.csv",
                    index=False)
    except Exception as e:
        print(f"The exception while getterUpdateAndSetterPositionId is {e}")
        pid = getterUpdateAndSetterPositionId(rDate, lock)
    return pid


# print(getterUpdateAndSetterPositionId())
