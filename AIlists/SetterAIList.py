import pandas as pd


def setterAIList(lock, df, fileName):
    lock.acquire()
    df.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlists\\AIstate\\{fileName}.csv", index=False)
    lock.release()
