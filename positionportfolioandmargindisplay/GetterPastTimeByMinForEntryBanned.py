import pandas as pd


def getterPastTimeByMinForEntryBanned():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\positionportfolioandmargindisplay\\displaystate\\PastTimeByMinEB.csv")
    except Exception as e:
        print(f"The exception while getter getterPastTimeByMinForEntryBanned is {e}")
        df = getterPastTimeByMinForEntryBanned()
    return df


# print(getterPastTimeByMin())
