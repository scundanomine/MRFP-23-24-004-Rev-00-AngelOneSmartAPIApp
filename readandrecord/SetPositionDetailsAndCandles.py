import datetime
import pandas as pd
from pastthirtycandles.GetterSpecificPastThirtyCandlesData import getterSpecificPastThirtyCandlesData


def setPositionDetailsAndCandles(pid, uid, symbol, row, cv, reportDate):
    # setting position details
    row["tOP"] = datetime.datetime.now() - cv
    dq = pd.DataFrame([row])
    dq.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positiondetails\\{pid}.csv", index=False)

    # setting position candles
    df = getterSpecificPastThirtyCandlesData(uid, symbol)
    df.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positioncandles\\{pid}.csv", index=False)