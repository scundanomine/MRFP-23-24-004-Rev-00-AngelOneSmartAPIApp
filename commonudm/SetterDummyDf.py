import pandas as pd


def setterDummyDf():
    sdf = pd.DataFrame(columns=['time', 'O', 'H', 'L', 'C', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc', 'um', 'dm', 'rsi'], index=range(10))
    sdf["atr"] = 0
    sdf["bulRP"] = "none"
    sdf["berRP"] = "none"
    sdf["roc"] = 0
    sdf["rsi"] = 50
    sdf["um"] = 0
    sdf["dm"] = 0
    sdf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\dummyDf.csv", index=False)

