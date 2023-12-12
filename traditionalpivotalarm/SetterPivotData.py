import pandas as pd


def setterPivotData(pivDf=pd.DataFrame()):
    pivDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\PivotData.csv",
        index=False)


# setterPivotData()
