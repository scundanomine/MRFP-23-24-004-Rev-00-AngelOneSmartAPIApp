import pandas as pd


def getterAIList(fileName):
    try:
        df = pd.read_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlists\\AIstate\\{fileName}.csv")
    except:
        # print(f"The exception while getterAIList is {e}")
        df = getterAIList(fileName)
    return df
