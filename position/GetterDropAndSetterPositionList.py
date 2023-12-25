import pandas as pd


def getterDropAndSetterPositionList(uid):
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
        i = df[(df.id == uid)].index
        df = df.drop(i)
        df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv", index=False)
    except Exception as e:
        print(f"The exception while getter, Drop and setter position List is {e}")

