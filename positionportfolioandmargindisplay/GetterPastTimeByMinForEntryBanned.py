import pandas as pd


def getterPastTimeByMinForEntryBanned():
    try:
        df = pd.read_csv(
            "F:\\AT\\positionportfolioandmargindisplay\\displaystate\\PastTimeByMinEB.csv")
    except Exception as e:
        print(f"The exception while getter getterPastTimeByMinForEntryBanned is {e}")
        df = getterPastTimeByMinForEntryBanned()
    return df


# print(getterPastTimeByMin())
