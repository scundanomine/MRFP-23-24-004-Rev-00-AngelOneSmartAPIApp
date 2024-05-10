import pandas as pd

from commonudm.SetterDummyDf import setterDummyDf


def getterDummyDf():
    try:
        df = pd.read_csv("F:\\AT\\eventloop\\eventstate\\dummyDf.csv")
    except Exception as e:
        print(f"The exception while getter Order list is {e}")
        setterDummyDf()
        df = pd.read_csv("F:\\AT\\eventloop\\eventstate\\dummyDf.csv")
    return df
