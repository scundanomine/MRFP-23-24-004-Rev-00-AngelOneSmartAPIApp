import pandas as pd


def setterPDS(df=pd.DataFrame()):
    df.to_csv("F:\\AT\\ohlcdata\\ohlcstate\\pastohlcdatafile\\pds.csv", index=False)

