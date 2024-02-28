import pandas as pd
from commonudm.GetterStockQtn import getterStockQtn


def setterPrePdsFdsAndFfdsList():
    n = getterStockQtn()
    df = pd.DataFrame(columns=list(range(6)), index=list(range(n)))
    df[:] = 0
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pastohlcdatafile\\pds.csv",
        index=False)
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\fds.csv",
        index=False)
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\futureohlcdatafile\\ffds.csv",
        index=False)
    return df


# setterPrePdsFdsAndFfdsList()
