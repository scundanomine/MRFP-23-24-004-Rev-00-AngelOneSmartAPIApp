import pandas as pd


def getterECBList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv")
    except Exception as e:
        print(f"The exception while getterECBList is {e}")
        df = getterECBList()
    return df


# getterECBList()
