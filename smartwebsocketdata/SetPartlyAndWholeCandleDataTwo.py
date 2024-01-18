import datetime
import pandas as pd


def setPartlyAndWholeCandleDataTwo(msg):
    try:
        time = datetime.datetime.fromtimestamp(msg['exchange_timestamp'] / 1000).isoformat()[:16] + ":00+05:30"
        ltp = msg['last_traded_price'] / 100
        volume = msg['volume_trade_for_the_day']
        token = msg['token']
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv")
        pTime = df.loc[0, '0']
        if pTime == 0:
            df.iloc[0] = [time, ltp, ltp, ltp, ltp, 0, volume, volume]
            df.to_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv",
                index=False)
        elif pTime != time:
            df['5'] = df['7'] - df['6']
            df.to_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisewholecandledata\\{token}.csv",
                index=False)
            df.iloc[0] = [time, ltp, ltp, ltp, ltp, 0, volume, volume]
            df.to_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv",
                index=False)
        else:
            df.loc[0, '4'] = ltp
            df.loc[0, '7'] = volume
            df.loc[0, '0'] = time
            if df.loc[0, '2'] < ltp:
                df.loc[0, '2'] = ltp
            if df.loc[0, '3'] > ltp:
                df.loc[0, '3'] = ltp
            df.to_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv",
                index=False)
    except Exception as e:
        print(f"Exception while inserting tick data from websocket One is {e}")
        pass

