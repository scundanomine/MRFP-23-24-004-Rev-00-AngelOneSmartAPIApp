import pandas as pd


def getterNiftySLDf():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\belliprogressionem\\state\\NiftySL.csv")
    except Exception as e:
        print(f"The exception while getterNiftySLDf is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterNiftySLDf()
    return df


# print(getterNiftySLDf())
