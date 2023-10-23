import time

import pandas as pd

from commonudm.GetSymbolAndToken import *
from AngelOneSmartAPIApp.test import *

dfc = pd.DataFrame()
m = 500
p = 60
i = 0
objOneX = []
objTwoX = []
exchange = "NSE"
stt = 0


def getCandlestickDataWithMultiProcessing(r, fileName, lock=""):
    startTime = time.time()
    global objOneX, objTwoX, dfc, p, i, stt
    dfc = getSymbolAndToken()
    ds = pd.DataFrame(index=list(range(r)), columns=['id', "O", "H", "L", "C", "V"])
    ds[:] = 0
    ds.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\LiveCandleData.csv", index=False)

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
        if uid < i - 3:
            try:
                data = getHistoricDataForOneDay(objOneX, "2023-10-20", str(b))[0]
            except:
                time.sleep(1)
                try:
                    data = getHistoricDataForOneDay(objOneX, "2023-10-20", str(b))[0]
                except:
                    data = {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        else:
            try:
                data = getHistoricDataForOneDay(objTwoX, "2023-10-20", str(b))[0]
            except:
                time.sleep(1)
                try:
                    data = getHistoricDataForOneDay(objTwoX, "2023-10-20", str(b))[0]
                except:
                    data = {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        # dfc.loc[uid, "ltp"] = ltp['data']['ltp']
        return data

    # main loop for thread
    ctrA = 0
    # while 300 - (time.time() - startTime) > 0:
    while ctrA < 1:
        ds = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\LiveCandleData.csv")
        ctr = 6
        for i in range(6, r + 6, 6):
            stt = time.time()
            with ThreadPoolExecutor() as executor:
                ltc = list(range(i - 6, i))
                results = executor.map(getCandleDataC, ltc)
                ck = ctr - 6
                for result in results:
                    ds.loc[ck, "id"] = ck + 1
                    ds.loc[ck, "O"] = result[1]
                    ds.loc[ck, "H"] = result[2]
                    ds.loc[ck, "L"] = result[3]
                    ds.loc[ck, "C"] = result[4]
                    ds.loc[ck, "V"] = result[5]
                    ck = ck + 1
            ctr = ctr + 6
            timeDiff = 1 - (time.time() - stt)
            if timeDiff > 0:
                time.sleep(timeDiff)
            # dtc.range(f"g{i-6+2}:k{i + 2}").options(pd.DataFrame, index=False, header=False).value = ds[i-6:i]
            ds.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\LiveCandleData.csv", index=False)
        ctrA = ctrA + 1
        print(f"{ctrA} execution time is {time.time() - startTime}")
        # break


getCandlestickDataWithMultiProcessing(300, "")
