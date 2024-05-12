import datetime
import pandas as pd
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from pastthirtycandles.GetterSpecificPastThirtyCandlesData import getterSpecificPastThirtyCandlesData


def setExitDetailsAndCandles(pid, uid, symbol, row, cv, reportDate):
    # setting position details
    row["tOEx"] = datetime.datetime.now() - cv
    dq = pd.DataFrame([row])
    dq.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitdetails\\{pid}.csv", index=False)

    # setting position candles
    df = getterSpecificPastThirtyCandlesData(uid, symbol)
    df.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitcandles\\{pid}.csv", index=False)

    # setting market position details
    dm = getterMarketStructureDf()
    dm.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitmdetails\\{pid}.csv",
        index=False)

    # setting position candles
    df = getterSpecificPastThirtyCandlesData(120, "Nifty 100")
    df.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitmcandles\\{pid}.csv",
        index=False)