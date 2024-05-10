import pandas as pd

from universallist.SetterDfThree import setterDfThree


def getterDfThree():
    try:
        uDf = pd.read_csv(
            "F:\\AT\\universallist\\liststate\\DfThree.csv")
    except Exception as e:
        print(f"Exception while getting Df Three list is {e}")
        uDf = getterDfThree()
    return uDf


# print(getterDfThree())
