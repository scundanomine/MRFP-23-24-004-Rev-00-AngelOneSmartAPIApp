from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from AngelOneSmartAPIApp.test import getAccessTokenOne

objOneX, accessTokenOneX = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")

AUTH_TOKEN = accessTokenOneX["authToken"]
API_KEY = "h7mCIfdW"
CLIENT_CODE = "J52460798"
FEED_TOKEN = accessTokenOneX["feedToken"]
correlation_id = "abc123"
action = 1
mode = 1
token_list = [
    {
        "exchangeType": 1,
        "tokens": ["2885",
                   "11536",
                   "1333",
                   "4963",
                   "1394",
                   "1594",
                   "1660"]
    }
]
sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)


def on_data(wsapp, message):
    logger.info("Ticks: {}".format(message))
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

sws.connect()
