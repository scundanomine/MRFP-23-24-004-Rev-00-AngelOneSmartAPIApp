from traditionalpivotalarm.GetSAndR import *
from AngelOneSmartAPIApp.test import *

objOneX = []
objTwoX = []
i = 0


def getLtpFromThreadMultipleLogin(objZ=0):
    global i, objOneX, objTwoX

    # get first login obj
    while True:
        try:
            objOneX, accessTokenOneX = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

        # get first login obj
    while True:
        try:
            objTwoX, accessTokenOneX = getAccessTokenOne("F5SzrULj", "S53761277", "8813", "2NF7QBQP7R3NEDXC4VN6UNWYWM")
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
        global objOneX, objTwoX
        a = mat["symbol"][uid]
        b = mat["token"][uid]
        if uid < 10:
            ltp = objOneX.ltpData(exchange, a, str(b))
        else:
            ltp = objTwoX.ltpData(exchange, a, str(b))
        # while True:
        #     try:
        #         ltp = obj.ltpData(exchange, a, str(b))
        #         break
        #     except Exception as e:
        #         print(f"Not getting ltp data due to {e}")
        #         time.sleep(1)
        return ltp['data']['ltp']

    results = []
    startTime = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        lt = list(range(20))
        results = executor.map(getLtpX, lt)
        index = i
        for result in results:
            mat.loc[index, "ltp"] = result
            index = index + 1
        mat.to_csv("mat.csv", index=False)

    print(mat["ltp"])
    print("--- %s seconds ---" % (time.perf_counter() - startTime))
    # mat.to_csv("mat.csv", index=False)


getLtpFromThreadMultipleLogin()
