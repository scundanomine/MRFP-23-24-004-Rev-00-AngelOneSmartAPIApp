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
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{rDate}\\state\\PId.csv",
                    index=False)
    except Exception as e:
        print(f"The exception while getterUpdateAndSetterPositionId is {e}")
        getterUpdateAndSetterPositionId(rDate, lock)
    return pid


# print(getterUpdateAndSetterPositionId())
