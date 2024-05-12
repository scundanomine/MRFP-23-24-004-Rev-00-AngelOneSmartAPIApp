import pandas as pd

from commonudm.SetterDummyDf import setterDummyDf


def getterDummyDf():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\dummyDf.csv")
    except Exception as e:
        print(f"The exception while getter Order list is {e}")
        setterDummyDf()
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\dummyDf.csv")
    return df
