from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from AngelOneSmartAPIApp.test import getAccessTokenOne
from commonudm.GetSymbolAndToken import getSymbolAndToken
from smartwebsocketdata.InsertTick import insertTick
from smartwebsocketdata.config import LIVE_FEED_JSON
import threading
import datetime

from smartwebsocketdata.SetPartlyAndWholeCandleData import setPartlyAndWholeCandleData

# tDf = getSymbolAndToken()
# tDf['token'] = tDf['token'].astype("str")
# tokenLst = tDf['token'].tolist()[:40]
tokenLst = ["2885"]

objOneX, accessTokenOneX = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")

AUTH_TOKEN = accessTokenOneX["authToken"]
API_KEY = "h7mCIfdW"
CLIENT_CODE = "J52460798"
FEED_TOKEN = accessTokenOneX["feedToken"]
correlation_id = "abc123"
action = 1
mode = 2
token_list = [
    {
        "exchangeType": 1,
        "tokens": tokenLst
    }
]
sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)


def on_data(wsapp, message):
    # logger.info("Ticks: {}".format(message))
    try:
        LIVE_FEED_JSON[message['token']] = {'time': datetime.datetime.fromtimestamp(message['exchange_timestamp']/1000).isoformat(), 'token': message['token'], 'ltp': message['last_traded_price'] / 100, 'volume': message['volume_trade_for_the_day']}
        print(LIVE_FEED_JSON)
        # insertTick(message)
        # setPartlyAndWholeCandleData(message)
    except Exception as e:
        print(e)
    # print(LIVE_FEED_JSON)
    # close_connection()


def on_open(wsapp):
    logger.info("on open")
    sws.subscribe(correlation_id, mode, token_list)


def on_error(wsapp, error):
    logger.error(error)


def on_close(wsapp):
    logger.info("Close")


def close_connection():
    sws.close_connection()


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

threading.Thread(target=sws.connect).start()
print("control release")
print(LIVE_FEED_JSON)


