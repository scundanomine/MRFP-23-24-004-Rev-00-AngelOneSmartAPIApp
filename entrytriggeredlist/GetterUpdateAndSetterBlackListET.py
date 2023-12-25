import pandas as pd

from entrytriggeredlist.GetCustomDfBlackListET import getCustomDfBlackListET


def getterUpdateAndSetterBlackListET(uid, value):
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv")
        df.loc[uid - 1, 'bFlag'] = value
        df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)
    except Exception as e:
        print(f"The exception while getter, update and setter ET black list is {e}")


