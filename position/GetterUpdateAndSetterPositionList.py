import pandas as pd


def getterUpdateAndSetterPositionList(uid, row, lock):
    try:
        with lock:
            df = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
            if uid in df['id'].values:
                i = df[(df.id == uid)].index
                df.iloc[i] = row
            df.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv",
                index=False)
    except Exception as e:
        print(f"The exception while getterUpdateAndSetterPositionList is {e}")
        getterUpdateAndSetterPositionList(uid, row, lock)
