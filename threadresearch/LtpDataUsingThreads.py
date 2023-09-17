from pivotalarm.GetSAndR import *
import time
from AngelOneSmartAPIApp.GetAccessToken import *
from concurrent.futures import ThreadPoolExecutor


def getLtpFromThread():
    global i
    startTime = time.perf_counter()
    obj, toc = get_access_token()
    exchange = "NSE"
    mat = getSRData()
    mat["ltp"] = 0

    # print(mat["ltp"])
    # print("--- %s seconds ---" % (time.perf_counter() - startTime))

    def getLtpX(uid):
        a = mat["symbol"][uid]
        b = mat["token"][uid]
        ltp = obj.ltpData(exchange, a, str(b))
        return ltp['data']['ltp']

    results = []
    for i in range(0, 210, 10):
        with ThreadPoolExecutor() as executor:
            # lt = list(range(len(mat["id"])))
            if i == 200:
                lt = list(range(i, i + 1))
            elif i > 200:
                break
            else:
                lt = list(range(i, i + 10))
            # print(lt)
            results = executor.map(getLtpX, lt)
            time.sleep(1.001)
            index = i
            for result in results:
                mat.loc[index, "ltp"] = result
                index = index + 1
            mat.to_csv("mat.csv", index=False)

    print(mat["ltp"])
    print("--- %s seconds ---" % (time.perf_counter() - startTime))
    # mat.to_csv("mat.csv", index=False)


getLtpFromThread()
