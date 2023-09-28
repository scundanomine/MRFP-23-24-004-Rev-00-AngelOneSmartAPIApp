from AngelOneSmartAPIApp.GetAccessToken import *
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd


def getHistoricDataForOneDay(obj, date, token):
    # obj, toc = get_access_token()
    start_time = time.time()
    candleStickData = []

    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": token,
            "interval": "ONE_DAY",
            "fromdate": f"{date} 00:00",
            "todate": f"{date} 15:30"
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    # time.sleep(0.53)
    return candleStickData["data"]


# print(getHistoricDataForOneDay("2023-09-28"))
