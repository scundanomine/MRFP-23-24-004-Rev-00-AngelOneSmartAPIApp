import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData


def setExitDetailsAndCandles(pid, uid, symbol, row, lock):
    # setting position details
    dq = pd.DataFrame(row)
    dq.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\exitdetails\\{pid}.csv", index=False)

    # setting position candles
    df = getterSpecificCandleData(uid, symbol, lock)
    df.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\exitcandles\\{pid}.csv", index=False)