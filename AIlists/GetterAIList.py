import pandas as pd


def getterAIList(fileName):
    df = pd.read_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlists\\AIstate\\{fileName}.csv")
    return df
