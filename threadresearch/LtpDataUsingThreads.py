from traditionalpivotalarm.GetSAndR import *
from AngelOneSmartAPIApp.test import *

obj = []
i = 0


def getLtpFromThread(objZ=0):
    global i, obj
    startTime = time.perf_counter()
    while True:
        try:
            obj, accessToken = get_access_token()
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)
    # obj = objZ
    exchange = "NSE"
    mat = getSRData()
    mat["ltp"] = 0

    # print(mat["ltp"])
    # print("--- %s seconds ---" % (time.perf_counter() - startTime))

    def getLtpX(uid):
        global obj
        a = mat["symbol"][uid]
        b = mat["token"][uid]
        ltp = obj.ltpData(exchange, a, str(b))
        # while True:
        #     try:
        #         ltp = obj.ltpData(exchange, a, str(b))
        #         break
        #     except Exception as e:
        #         print(f"Not getting ltp data due to {e}")
        #         time.sleep(1)
        return ltp['data']['ltp']

    results = []
    for i in range(0, 60, 10):
        time.sleep(1.001)
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
            index = i
            for result in results:
                mat.loc[index, "ltp"] = result
                index = index + 1
            mat.to_csv("mat.csv", index=False)

    print(mat["ltp"])
    print("--- %s seconds ---" % (time.perf_counter() - startTime))
    # mat.to_csv("mat.csv", index=False)

# getLtpFromThread()
