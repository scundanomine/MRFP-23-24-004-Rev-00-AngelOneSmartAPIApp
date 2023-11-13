import pandas as pd


def getterUniversalList():
    while True:
        try:
            uDf = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\universallist\\liststate\\UniversalList.csv")
            break
        except Exception as e:
            print(f"Exception while getting Universal getter list is {e}")
    return uDf
