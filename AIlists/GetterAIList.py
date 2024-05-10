import pandas as pd


def getterAIList(fileName):
    try:
        df = pd.read_csv(f"F:\\AT\\AIlists\\AIstate\\{fileName}.csv")
    except:
        # print(f"The exception while getterAIList is {e}")
        df = getterAIList(fileName)
    return df
