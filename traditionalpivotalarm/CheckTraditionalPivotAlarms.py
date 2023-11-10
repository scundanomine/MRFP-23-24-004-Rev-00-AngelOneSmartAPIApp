import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from commonudm.GetSymbolAndToken import getSymbolAndToken
from traditionalpivotalarm.GetSAndR import getSRData
from traditionalpivotalarm.TraditionalPivotAlarm import traditionalPivotAlarm


def checkTraditionalPivotAlarms(niftySize=300):
    startTime = time.time()

    # get token and symbol
    dst = getSymbolAndToken()

    # get sr data and sr list
    varSR = getSRData()
    srLst = varSR.to_dict('records')

    # dcs and dcs list
    dcs = pd.read_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\LiveCandleData.csv")
    dcsLst = dcs.to_dict('records')

    # define sub function
    def getDataAndCheckAlarm(uid):
        # time.sleep(0.2)
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
            recordedData = df.to_dict('records')[9]
        except Exception as e:
            print(f"given exception for {uid + 1} is {e}")
            recordedData = {"time": 0, "O": 0, "H": 0, "L": 0, "C": 0, "V": 0}
        alarmTimer, refT, srType, srValue, nSR = traditionalPivotAlarm(srLst[uid], dcsLst[uid], recordedData['C'])
        recordedData.update(
            {"alarmTimer": alarmTimer, "refT": refT, "srT": srType, "srV": srValue, "nSR": nSR})
        return recordedData

    with ThreadPoolExecutor() as executor:
        ltc = list(range(niftySize))
        results = executor.map(getDataAndCheckAlarm, ltc)
        ck = 0
        for result in results:
            dcs.loc[ck, "id"] = ck + 1
            dcs.loc[ck, "O"] = result["O"]
            dcs.loc[ck, "H"] = result["H"]
            dcs.loc[ck, "L"] = result["L"]
            dcs.loc[ck, "C"] = result["C"]
            dcs.loc[ck, "V"] = result["V"]
            dcs.loc[ck, "alarmTimer"] = result["alarmTimer"]
            dcs.loc[ck, "refT"] = result["refT"]
            dcs.loc[ck, "srT"] = result["srT"]
            dcs.loc[ck, "srV"] = result["srV"]
            dcs.loc[ck, "nSR"] = result["nsR"]
            ck = ck + 1
    dcs.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\LiveCandleData.csv",
        index=False)
    print(dcs)
    print(f"execution time is {time.time() - startTime}")


for k in range(100):
    checkTraditionalPivotAlarms()
# k = 0
# while k < 60:
#     getPreviousDataForPivotAlarm()
#     k = k + 1
