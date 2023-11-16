import pandas as pd
from entrytriggeredlist.GetterAndSetterAIList import getterAIList


def clearPreviousAIList():
    while True:
        try:
            aiDf = pd.read_csv(
                "/entrytriggeredlist\\AIstateE:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIList.csv")
            # deletion of All rows
            size = len(aiDf)
            aiDf = aiDf.drop(labels=range(size), axis=0)
            aiDf.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstateE:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIList.csv",
                index=False)
            break
        except Exception as e:
            print(f"Exception while clearing AI list is {e}")
            aiDf = getterAIList()
            aiDf.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstateE:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIList.csv",
                index=False)
