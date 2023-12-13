import pandas as pd

from universallist.SetterDfThree import setterDfThree


def getterDfThree():
    try:
        uDf = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\universallist\\liststate\\DfThree.csv")
    except Exception as e:
        print(f"Exception while getting Df Three list is {e}")
        uDf = setterDfThree()
    return uDf


# print(getterDfThree())
