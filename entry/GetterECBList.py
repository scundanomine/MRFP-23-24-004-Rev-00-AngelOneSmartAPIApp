import pandas as pd


def getterECBList():
    try:
        df = pd.read_csv("F:\\AT\\entry\\entrystate\\ECBList.csv")
    except Exception as e:
        print(f"The exception while getterECBList is {e}")
        df = getterECBList()
    return df


# getterECBList()
