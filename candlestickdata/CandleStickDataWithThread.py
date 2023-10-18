from AngelOneSmartAPIApp.GetAccessToken import *
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

candleStickData = []


def getCandleStickDataViaThreads(objC):
    global candleStickData
    # obj, toc = get_access_token()
    obj = objC

    # Historic api
    def getMultipleCandleStick(token):
        time.sleep(0.55)
        global candleStickData
        try:
            historicParam = {
                "exchange": "NSE",
                "symboltoken": token,
                "interval": "ONE_MINUTE",
                "fromdate": "2023-09-20 09:20",
                "todate": "2023-09-20 09:29"
            }
            candleStickData = obj.getCandleData(historicParam)
        except Exception as e:
            print("Historic Api failed: {}".format(e.message))
        # print(f"execution time is {time.time() - start_time}")

        return candleStickData

    with ThreadPoolExecutor() as executor:
        lt = ['13061', '474', '13']
        # print(lt)
        results = executor.map(getMultipleCandleStick, lt)
        for result in results:
            print(result["data"])


# startTimeTwo = time.time()
# for i in range(10):
#     print(getCandleStickDataViaThreads())
#     print(f"execution time is {time.time() - startTimeTwo}")
# df = pd.DataFrame(getCandleStickData()["data"])
# print(df)
