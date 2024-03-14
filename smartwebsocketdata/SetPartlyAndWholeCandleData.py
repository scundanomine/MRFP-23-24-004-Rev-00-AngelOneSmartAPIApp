import datetime
import pandas as pd
import time
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterTimeDelta import getterTimeDelta
import multiprocessing
from smartwebsocketdata.GetListOfTokensForSpecificNumber import getListOfTokensForSpecificNumber


def setPartlyAndWholeCandleData(r=30, lock=multiprocessing.Lock()):
    cv = pd.to_timedelta(0)
    lock.acquire()
    exitTime = getterExitTime()
    lock.release()
    tokenList = getListOfTokensForSpecificNumber(r - 30, r)
    while datetime.datetime.now() - cv < exitTime:
        for token in tokenList:
            while True:
                try:
                    cdf = pd.read_csv(
                        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisefreshcandledata\\{token}.csv")
                    break
                except Exception as e:
                    print(f"Exception while reading {token} from tokenwisefreshcandledata is {e}")
            timeOne = datetime.datetime.fromtimestamp(cdf.loc[0, '0'] / 1000).isoformat()[:16] + ":00+05:30"
            ltp = cdf.loc[0, '1'] / 100
            volume = cdf.loc[0, '2']

            while True:
                try:
                    df = pd.read_csv(
                        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv")
                    break
                except Exception as e:
                    print(f"Exception while reading {token} from tokenwisepartlycandledata is {e}")

            pTime = df.loc[0, '0']
            if pTime == 0:
                df.iloc[0] = [timeOne, ltp, ltp, ltp, ltp, 0, volume, volume]
                df.to_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv",
                    index=False)
            elif pTime != timeOne:
                df['5'] = df['7'] - df['6']
                df.to_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisewholecandledata\\{token}.csv",
                    index=False)
                df.iloc[0] = [timeOne, ltp, ltp, ltp, ltp, 0, volume, volume]
                df.to_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv",
                    index=False)
            else:
                df.loc[0, '4'] = ltp
                df.loc[0, '7'] = volume
                df.loc[0, '0'] = timeOne
                if df.loc[0, '2'] < ltp:
                    df.loc[0, '2'] = ltp
                if df.loc[0, '3'] > ltp:
                    df.loc[0, '3'] = ltp
                df.to_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv",
                    index=False)
            # time.sleep(1/120)
