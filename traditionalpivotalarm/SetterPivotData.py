import pandas as pd


def setterPivotData(pivDf=pd.DataFrame()):
    pivDf.to_csv(
        "F:\\AT\\traditionalpivotalarm\\pivotstate\\PivotData.csv",
        index=False)


# setterPivotData()
