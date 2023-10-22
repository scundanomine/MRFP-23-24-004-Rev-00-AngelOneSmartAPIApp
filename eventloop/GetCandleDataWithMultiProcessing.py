from commonudm.GetSymbolAndToken import *
from AngelOneSmartAPIApp.test import *

dfc = pd.DataFrame()
m = 500
p = 60
i = 0
objOneX = []
objTwoX = []
exchange = "NSE"


def getCandlestickDataWithMultiProcessing(r, fileName, lock=""):
    startTime = time.time()
    global objOneX, objTwoX, dfc, p, i
    dfc = getSymbolAndToken()
    ds = pd.DataFrame(index=list(range(r)))

    # data instance for excel
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")

    # getting big dataframe
    dtc = wb.sheets("Sheet3")
    # creating session one
    while True:
        try:
            print("getting obj1")
            objOneX, accessTokenOneX = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    # creating session two
    while True:
        try:
            print("getting obj2")
            objTwoX, accessTokenOneX = getAccessTokenOne("F5SzrULj", "S53761277", "8813", "2NF7QBQP7R3NEDXC4VN6UNWYWM")
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)

    def getCandleDataC(uid):
        global objOneX, objTwoX, dfc, i
        b = dfc["token"][uid]
        # if uid < i - 3:
        data = getHistoricDataForOneDay(objOneX, "2023-10-20", str(b))[0]
        # else:
        #     data = getHistoricDataForOneDay(objTwoX, "2023-10-20", str(b))[0]
        # dfc.loc[uid, "ltp"] = ltp['data']['ltp']
        return data

    # main loop for thread
    ctrA = 0
    # while 300 - (time.time() - startTime) > 0:
    while ctrA == 0:
        ds[:] = 0
        ctr = 6
        for i in range(6, r + 6, 6):
            with ThreadPoolExecutor() as executor:
                ltc = list(range(i - 6, i))
                results = executor.map(getCandleDataC, ltc)
                ck = ctr - 6
                for result in results:
                    ds.loc[ck, 0] = result[1]
                    ds.loc[ck, 1] = result[2]
                    ds.loc[ck, 2] = result[3]
                    ds.loc[ck, 3] = result[4]
                    ds.loc[ck, 4] = result[5]
                    ck = ck + 1
            ctr = ctr + 6
            time.sleep(1)
        dtc.range(f"g{2}:k{r + 2}").options(pd.DataFrame, index=False, header=False).value = ds
        # ds.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\{fileName}")
        ctrA = ctrA + 1
        print(f"{ctrA} execution time is {time.time() - startTime}")
        break


getCandlestickDataWithMultiProcessing(204, "")
