import pandas as pd


def getterPositionList():
    try:
        df = pd.read_csv("F:\\AT\\position\\positionstate\\PositionList.csv")
    except:
        # print(f"The exception while getter Position list is {e}")
        df = getterPositionList()
    return df


# getterEntryList()
