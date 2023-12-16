import pandas as pd


def getterECBList(lock):
    try:
        lock.acquire()
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv")
        lock.release()
    except Exception as e:
        print(f"The exception while getter ET black list is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        lock.acquire()
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\SymbolAndToken.csv")
        lock.release()
        df = df.loc[:, ['id']]
        # flag for entry calculation
        df['eCBFlag'] = False
        lock.acquire()
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv",
            index=False)
        lock.release()
    return df


# getterECBList()
