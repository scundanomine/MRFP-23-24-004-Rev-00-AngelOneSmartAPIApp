import pandas as pd


def setterAIList(df, fileName):
    df.to_csv(f"F:\\AT\\AIlists\\AIstate\\{fileName}.csv", index=False)
