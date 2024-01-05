import pandas as pd


def getterAIList(fileName, lock):
    try:
        with lock:
            df = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlists\\AIstate\\{fileName}.csv")
    except Exception as e:
        print(f"The exception while getter AI list is {e}")
        df = pd.DataFrame()
    return df
