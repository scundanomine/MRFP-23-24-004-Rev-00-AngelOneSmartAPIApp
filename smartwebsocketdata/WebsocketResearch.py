from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
import time

from AngelOneSmartAPIApp.test import getAccessTokenOne

# creating session one
while True:
    try:
        print("getting obj1")
        objOneX, accessTokenOneX = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")
        break
    except Exception as e:
        print(f"Not getting accessToken due to {e}")
        time.sleep(1)

AUTH_TOKEN = accessTokenOneX["authToken"]
API_KEY = "h7mCIfdW"
CLIENT_CODE = "J52460798"
FEED_TOKEN = accessTokenOneX["feedToken"]
correlation_id = "abc123"
action = 1
mode = 1
token_list = [{"exchangeType": "1", "tokens": ["2885"]}]

# retry_strategy=0 for simple retry mechanism
sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)


def on_data(wsapp, message):
    logger.info("Ticks: {}".format(message))
    # close_connection()


def on_control_message(wsapp, message):
    logger.info(f"Control Message: {message}")


def on_open(wsapp):
    logger.info("on open")
    some_error_condition = False
    if some_error_condition:
        error_message = "Simulated error"
        if hasattr(wsapp, 'on_error'):
            wsapp.on_error("Custom Error Type", error_message)
    else:
        sws.subscribe(correlation_id, mode, token_list)
        # sws.unsubscribe(correlation_id, mode, token_list1)


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
sws.on_control_message = on_control_message

sws.connect()