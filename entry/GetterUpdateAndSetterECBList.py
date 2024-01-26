import pandas as pd

from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET


def getterUpdateAndSetterECBList(uid, value):
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv")
        df.loc[uid - 1, 'eCBFlag'] = value
        df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv", index=False)
    except Exception as e:
        print(f"The exception while getterUpdateAndSetterECBList is {e}")
        getterUpdateAndSetterECBList(uid, value)


