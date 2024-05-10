import datetime
import pandas as pd


def setFreshCandleDataOne(msg):
    try:
        df = pd.DataFrame([[msg['exchange_timestamp'], msg['last_traded_price'], msg['volume_trade_for_the_day']]])
        df.to_csv(
                    f"F:\\AT\\smartwebsocketdata\\websocketstate\\tokenwisefreshcandledata\\{msg['token']}.csv",
                    index=False)
    except Exception as e:
        print(f"Exception while setFreshCandleDataOne from websocket One is {e}")

