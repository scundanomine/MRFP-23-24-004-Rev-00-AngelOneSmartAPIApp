import pandas as pd


def setterFFDS(df=pd.DataFrame()):
    df.to_csv("F:\\AT\\ohlcdata\\ohlcstate\\futureohlcdatafile\\ffds.csv", index=False)

