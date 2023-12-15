import pandas as pd


def getterEntryTriggeredList(lock):
    try:
        lock.aquire()
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv")
        lock.release()
    except Exception as e:
        print(f"The exception while getter Order list is {e}")
        df = pd.DataFrame(columns=['id', 'ol'])
        lock.aquire()
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv",
            index=False)
        lock.release()
    return df
