import pandas as pd
from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData
import datetime


def setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate):
    # setting position details
    row["tOEx"] = datetime.datetime.now() - cv
    dq = pd.DataFrame([row])
    dq.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitdetails\\{pid}.csv", index=False)

    # setting position candles
    df = getterSpecificCandleData(uid, symbol)
    df.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitcandles\\{pid}.csv", index=False)