import os
from concurrent.futures import ThreadPoolExecutor
from AngelOneSmartAPIApp.test import *
from commonudm.GetSymbolAndToken import getSymbolAndToken
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from eventloop.CreateGSTDataFile import *
from historicdata.HistoricDataForOneMinuteForTraditionalPivot import historicDataForOneMinuteForTraditionalPivot
from historicdata.ParsingHistoricDataWithDateTime import parsingHistoricDataWithDateTime


def getSpecificDateHistoricDataUsingSmartApi(c):
    # getter required symbol and token
    gDf = getterRequiredSymbolAndTokenList()
    r = len(gDf)
    # create date folder if doesn't exit
    if not os.path.exists(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\historicdata\\historicdatastate\\{c}"):
        os.makedirs(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\historicdata\\historicdatastate\\{c}")
    print("Process for past 10 candles data started")
    startTime = time.time()
    dfc = getSymbolAndToken()
    # c = getterTimeDelta()
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

    def getCandleFirstDataC(uid):
        b = dfc["token"][uid]
        a = dfc["symbol"][uid]
        flagZero = False
        if uid < i - 3:
            try:
                data = historicDataForOneMinuteForTraditionalPivot(objOneX, c, str(b))
            except:
                time.sleep(1)
                try:
                    data = historicDataForOneMinuteForTraditionalPivot(objOneX, c, str(b))
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
        else:
            try:
                data = historicDataForOneMinuteForTraditionalPivot(objTwoX, c, str(b))
            except:
                time.sleep(1)
                try:
                    data = historicDataForOneMinuteForTraditionalPivot(objTwoX, c, str(b))
                except:
                    data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
        dfT = pd.DataFrame(data)
        sid = uid + 1
        dfT.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\historicdata\\historicdatastate\\{c}\\{sid}.csv", index=False)
        # processPastTenCandlesData(uid + 1, a, rfTime, flagZero, dfT)
        # getFirstItrCandlesticksProperties(uid+1, a)

    # main loop for thread
    for i in range(6, r + 6, 6):
        stt = time.time()
        with ThreadPoolExecutor() as executor:
            ltc = list(range(i - 6, i))
            executor.map(getCandleFirstDataC, ltc)
            time.sleep(1)
    for j in range(r):
        parsingHistoricDataWithDateTime(c, j+1)

    print(f"The execution time is {time.time() - startTime}")


getSpecificDateHistoricDataUsingSmartApi("2024-04-16")
