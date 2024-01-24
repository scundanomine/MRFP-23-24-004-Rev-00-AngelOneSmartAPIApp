import time
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from AngelOneSmartAPIApp.test import getAccessTokenOne
from smartwebsocketdata.GetterSpecificTokenListForWebSocket import getterSpecificTokenListForWebSocket
from smartwebsocketdata.SetFreshCandleDataTwo import setFreshCandleDataTwo


def smartApiWebSocketTwo(lock):
    tokenLst = getterSpecificTokenListForWebSocket("TokenList1")

    # creating session two
    while True:
        try:
            print("getting obj2")
            objTwoY, accessTokenOneY = getAccessTokenOne("F5SzrULj", "S53761277", "8813", "2NF7QBQP7R3NEDXC4VN6UNWYWM")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    AUTH_TOKEN = accessTokenOneY["authToken"]
    API_KEY = "h7mCIfdW"
    CLIENT_CODE = "S53761277"
    FEED_TOKEN = accessTokenOneY["feedToken"]
    correlation_id = "abc1234"
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
            setFreshCandleDataTwo(message)
        except Exception as eOne:
            print(eOne)

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

    print("process for websocket two just started wow!!!!!!!!!!!")
    # threading.Thread(target=sws.connect).start()
    sws.connect()
    print("control release for websocket 2")


# smartApiWebSocketOne()
