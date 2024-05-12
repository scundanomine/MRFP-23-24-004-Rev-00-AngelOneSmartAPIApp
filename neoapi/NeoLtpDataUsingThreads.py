from commonudm.GetSymbolAndToken import *
# from AngelOneSmartAPIApp.test import *
from neoapi.NeoApiAccessToken import getKotakNeoApiAccessToken
from concurrent.futures import ThreadPoolExecutor
import time

dfc = pd.DataFrame()
m = 500
p = 60
i = 0
client = []
objTwoX = []
exchange = "NSE"
stt = 0


def getNeoLtpDataUsingThreads(r, fileName, lock="", c=""):
    startTime = time.time()
    global client, objTwoX, dfc, p, i, stt
    dfc = getSymbolAndToken()
    ds = pd.DataFrame(index=list(range(r)), columns=['id', "ltp"])
    ds[:] = 0
    ds.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\neoapi\\neoapistate\\NeoLiveCandleData.csv",
        index=False)

    # data instance for excel
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting big dataframe
    dtc = wb.sheets("Sheet3")
    # creating session one
    while True:
        try:
            print("getting obj1")
            client = getKotakNeoApiAccessToken()
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    # creating session two
    # while True:
    #     try:
    #         print("getting obj2")
    #         objTwoX, accessTokenOneX = getAccessTokenOne("F5SzrULj", "S53761277", "8813", "2NF7QBQP7R3NEDXC4VN6UNWYWM")
    #         break
    #     except Exception as e:
    #         print(f"Not getting accessToken due to {e}")
    #         time.sleep(1)

    def getNeoLtpDataC(uid):
        global client, objTwoX, dfc, i
        b = dfc["token"][uid]
        a = dfc["symbol"][uid]
        # if uid < i - 3:
        try:
            data = client.quote(instrument_token=b, quote_type="LTP")
        except:
            time.sleep(1)
            try:
                data = client.quote(instrument_token=b, quote_type="LTP")
            except:
                data = 0
                print("Exception when calling Quoate api -> quote_details: %s\n % e")
        # else:
        #     try:
        #         data = getHistoricDataForOneDay(objTwoX, c, str(b))[0]
        #     except:
        #         time.sleep(1)
        #         try:
        #             data = getHistoricDataForOneDay(objTwoX, c, str(b))[0]
        #         except:
        #             data = {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        # dfc.loc[uid, "ltp"] = ltp['data']['ltp']
        return data

    # main loop for thread
    ctrA = 0
    # while 300 - (time.time() - startTime) > 0:
    while ctrA < 1:
        ds = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\neoapi\\neoapistate\\NeoLiveCandleData.csv")
        ctr = 10
        for i in range(10, r + 10, 10):
            stt = time.time()
            with ThreadPoolExecutor() as executor:
                ltc = list(range(i - 10, i))
                results = executor.map(getNeoLtpDataC, ltc)
                ck = ctr - 10
                for result in results:
                    ds.loc[ck, "id"] = ck + 1
                    ds.loc[ck, "ltp"] = result
                    ck = ck + 1
            ctr = ctr + 10
            timeDiff = 1 - (time.time() - stt)
            if timeDiff > 0:
                time.sleep(timeDiff)
            # dtc.range(f"g{i-6+2}:k{i + 2}").options(pd.DataFrame, index=False, header=False).value = ds[i-6:i]
            ds.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\neoapi\\neoapistate\\NeoLiveCandleData.csv",
                index=False)
        ctrA = ctrA + 1
        print(f"{ctrA} execution time is {time.time() - startTime}")
        # break


getNeoLtpDataUsingThreads(50, "")
