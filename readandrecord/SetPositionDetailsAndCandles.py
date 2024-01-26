import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData


def setPositionDetailsAndCandles(pid, uid, symbol, row):
    # setting position details
    dq = pd.DataFrame(row)
    dq.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\positiondetails\\{pid}.csv", index=False)

    # setting position candles
    df = getterSpecificCandleData(uid, symbol)
    df.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\positioncandles\\{pid}.csv", index=False)