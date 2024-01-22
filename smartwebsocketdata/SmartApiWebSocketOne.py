from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from AngelOneSmartAPIApp.test import getAccessTokenOne
from smartwebsocketdata.GetterSpecificTokenListForWebSocket import getterSpecificTokenListForWebSocket
from smartwebsocketdata.SetPartlyAndWholeCandleData import setPartlyAndWholeCandleData
import time


def smartApiWebSocketOne(lock):
    tokenLst = getterSpecificTokenListForWebSocket("TokenList0")

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
    mode = 2
    token_list = [
        {
            "exchangeType": 1,
            "tokens": tokenLst
        }
    ]
    sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)

    def on_data(wsapp, message):
        try:
            setPartlyAndWholeCandleData(message, lock)
        except Exception as e:
            print(e)

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

    print("process for websocket one just started wow!!!!!!!!!!!")
    # threading.Thread(target=sws.connect).start()
    sws.connect()
    print("control release for Websocket One")


# smartApiWebSocketOne()
