from AngelOneSmartAPIApp.GetAccessToken import *


def getLiveData(objs, symbol, token):
    # global kite, live_data
    # obj, toc = get_access_token()
    exchange = "NSE"

    ltp = objs.ltpData(exchange, symbol, token)
    return ltp['data']


# print(getLiveData("JINDALSTEL-EQ", "6733"))
