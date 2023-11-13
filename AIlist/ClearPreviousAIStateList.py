import pandas as pd
from AIlist.GetterAIStateList import getterAIStateList


def clearPreviousAIList(niftySize):
    while True:
        try:
            sDf = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstateE:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIStateList.csv")
            # deletion of All rows
            sDf = sDf.drop(labels=range(niftySize), axis=0)
            sDf.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstateE:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIStateList.csv",
                index=False)
            break
        except Exception as e:
            print(f"Exception while clearing AI list is {e}")
            sDf = getterAIStateList(niftySize)
            sDf.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstateE:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIStateList.csv",
                index=False)
