import pandas as pd


def getterUniversalList():
    try:
        uDf = pd.read_csv(
            "F:\\AT\\universallist\\liststate\\UniversalList.csv")
    except:
        # print(f"Exception while getting Universal getter list is {e}")
        uDf = getterUniversalList()
    return uDf
