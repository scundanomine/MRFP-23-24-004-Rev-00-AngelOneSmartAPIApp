import pandas as pd


def setterFDS(df=pd.DataFrame()):
    df.to_csv("F:\\AT\\ohlcdata\\ohlcstate\\futureohlcdatafile\\fds.csv", index=False)

