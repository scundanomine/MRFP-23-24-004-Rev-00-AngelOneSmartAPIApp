from AngelOneSmartAPIApp.GetAccessToken import *
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd


def getCandleStickData():
    obj, toc = get_access_token()
    start_time = time.time()
    candleStickData = []

    # Historic api
    def getMultipleCandleStick():
        pass

    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": "2277",
            "interval": "THREE_MINUTE",
            "fromdate": "2023-09-20 09:15",
            "todate": "2023-09-20 09:44"
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    # print(f"execution time is {time.time() - start_time}")
    time.sleep(0.53)
    return candleStickData["data"]


# startTimeTwo = time.time()
# for i in range(120):
#     print(getCandleStickData()["data"])
#     print(f"execution time is {time.time() - startTimeTwo}")
# df = pd.DataFrame(getCandleStickData()["data"])
# print(df)
