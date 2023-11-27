import pandas as pd


def getterECBList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv")
    except Exception as e:
        print(f"The exception while getter ET black list is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\SymbolAndToken.csv")
        df = df.loc[:, ['id']]
        # flag for entry calculation
        df['eCBFlag'] = False
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv",
            index=False)
    return df


# getterECBList()
