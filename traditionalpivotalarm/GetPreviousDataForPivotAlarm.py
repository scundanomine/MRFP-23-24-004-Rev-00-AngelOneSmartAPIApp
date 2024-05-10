import time

import pandas as pd
from concurrent.futures import ThreadPoolExecutor

from commonudm.GetSymbolAndToken import getSymbolAndToken


def getPreviousDataForPivotAlarm(niftySize=300):
    startTime = time.time()
    # get token and symbol
    dst = getSymbolAndToken()

    # provision of dcs
    dcs = pd.DataFrame(index=list(range(niftySize)),
                       columns=['id', "O", "H", "L", "C", "V", "alarmTimer", "refT", "srT", "srV", "nSR", "GL"])
    dcs[:] = 0
    dcs.to_csv(
        "F:\\AT\\traditionalpivotalarm\\pivotstate\\LiveCandleData.csv",
        index=False)

    # define sub function
    def getPreviousData(uid):
        # time.sleep(0.2)
        symbol = dst["symbol"][uid]
        try:
            df = pd.read_csv(
                f"F:\\AT\\eventloop\\eventstate\\candlewisedata\\{uid + 1}_{symbol}.csv")
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

    with ThreadPoolExecutor() as executor:
        ltc = list(range(niftySize))
        results = executor.map(getPreviousData, ltc)
        ck = 0
        for result in results:
            dcs.loc[ck, "id"] = ck + 1
            dcs.loc[ck, "O"] = result["O"]
            dcs.loc[ck, "H"] = result["H"]
            dcs.loc[ck, "L"] = result["L"]
            dcs.loc[ck, "C"] = result["C"]
            dcs.loc[ck, "V"] = result["V"]
            ck = ck + 1
    dcs.to_csv(
        "F:\\AT\\traditionalpivotalarm\\pivotstate\\LiveCandleData.csv",
        index=False)
    print(dcs)
    print(f"execution time is {time.time() - startTime}")


getPreviousDataForPivotAlarm()
# k = 0
# while k < 60:
#     getPreviousDataForPivotAlarm()
#     k = k + 1
