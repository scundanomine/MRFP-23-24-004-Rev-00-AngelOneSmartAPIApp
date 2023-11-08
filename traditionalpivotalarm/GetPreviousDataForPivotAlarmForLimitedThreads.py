import time

import pandas as pd
from concurrent.futures import ThreadPoolExecutor

from commonudm.GetSymbolAndToken import getSymbolAndToken


def getPreviousDataForPivotAlarmForLimitedThreads(niftySize=300, threadSize=50):
    startTime = time.time()
    # get token and symbol
    dst = getSymbolAndToken()

    # provision of dcs
    dcs = pd.DataFrame(index=list(range(niftySize)),
                       columns=['id', "O", "H", "L", "C", "V", "alarmTimer", "refT", "srT", "srV"])
    dcs[:] = 0
    dcs.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\LiveCandleData.csv",
        index=False)

    # define sub function
    def getPreviousDataForLimitedThreads(uid):
        # time.sleep(0.1)
        symbol = dst["symbol"][uid]
        try:
            df = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{uid + 1}_{symbol}.csv")
        except:
            data = [{0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                    {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                    {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                    {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                    {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, {0: "", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}]
            df = pd.DataFrame(data)
            # rename ohlc
            df.rename(columns={0: "time", 1: "O", 2: "H", 3: "L", 4: "C", 5: "V"}, inplace=True)
        try:
            return df.to_dict('records')[9]
        except Exception as e:
            print(f"given exception for {uid + 1} is {e}")
            return {"time": 0, "O": 0, "H": 0, "L": 0, "C": 0, "V": 0}

    for i in range(threadSize, niftySize + threadSize, threadSize):
        with ThreadPoolExecutor() as executor:
            ltc = list(range(i-threadSize, i))
            results = executor.map(getPreviousDataForLimitedThreads, ltc)
            ck = i-threadSize
            for result in results:
                dcs.loc[ck, "id"] = ck + 1
                dcs.loc[ck, "O"] = result["O"]
                dcs.loc[ck, "H"] = result["H"]
                dcs.loc[ck, "L"] = result["L"]
                dcs.loc[ck, "C"] = result["C"]
                dcs.loc[ck, "V"] = result["V"]
                ck = ck + 1
    dcs.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\LiveCandleData.csv",
        index=False)
    print(dcs)
    print(f"execution time is {time.time() - startTime}")


k = 0
while k < 60:
    getPreviousDataForPivotAlarmForLimitedThreads()
    k = k + 1
