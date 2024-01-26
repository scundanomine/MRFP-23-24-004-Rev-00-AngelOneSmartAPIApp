import multiprocessing
import pandas as pd


def getterUpdateAndSetterPositionId(lock=multiprocessing.Lock()):
    try:
        with lock:
            df = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PId.csv")
            df.loc[0, 'pid'] = df.loc[0, 'pid'] + 1
            sid = df.loc[0, 'pid']
            df.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PId.csv",
                index=False)
    except Exception as e:
        print(f"The exception while getterUpdateAndSetterPositionId is {e}")
        sid = getterUpdateAndSetterPositionId(lock)
    return sid


# print(getterUpdateAndSetterPositionId())
